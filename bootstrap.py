#!/usr/bin/env python3
"""Instala setup-roy en el proyecto actual (humano o IA).

Copia solo setup-roy/ → docs/setup-roy/ y añade el snippet en AGENTS.md
si falta el marcador ## Setup Roy.
No copia README, INSTALL ni este script al proyecto.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SNIPPET = """## Setup Roy
If the request may be covered by the pack under `docs/setup-roy/`, read `docs/setup-roy/agents.md` first and follow its index. Otherwise work normally.
"""

SNIPPET_MARKER = "## Setup Roy"


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr, flush=True)
    raise SystemExit(code)


def info(msg: str) -> None:
    print(msg, flush=True)


def find_pack_root(source: Path) -> Path:
    """Acepta la raíz del repo setup-ia o la carpeta setup-roy/."""
    source = source.resolve()
    if not source.exists():
        die(f"no existe la ruta de origen: {source}")
    if not source.is_dir():
        die(f"el origen debe ser un directorio: {source}")

    nested = source / "setup-roy" / "agents.md"
    if nested.is_file():
        return source / "setup-roy"

    if (source / "agents.md").is_file() and source.name == "setup-roy":
        return source

    die(
        "no encontré el pack setup-roy.\n"
        f"  Busqué: {source / 'setup-roy' / 'agents.md'}\n"
        f"  O bien: {source}/agents.md (si la carpeta se llama setup-roy)\n"
        "  Pasa la raíz del repo setup-ia o la carpeta setup-roy/."
    )


def ensure_git() -> None:
    if shutil.which("git") is None:
        die(
            "no está disponible el comando `git` (hace falta para --repo).\n"
            "  Instala git, o usa --from con una copia local del repo."
        )


def clone_repo(repo: str, dest: Path) -> Path:
    ensure_git()
    info(f"clonando {repo} …")
    result = subprocess.run(
        ["git", "clone", "--depth", "1", repo, str(dest)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip() or "(sin detalle)"
        die(
            f"falló git clone de {repo}\n"
            f"  Detalle: {detail}\n"
            "  Comprueba la URL, la red y el acceso al repo."
        )
    return find_pack_root(dest)


def copy_pack(pack: Path, target: Path, *, force: bool, dry_run: bool) -> None:
    if not (pack / "agents.md").is_file():
        die(f"el pack de origen no tiene agents.md: {pack}")

    if target.exists():
        if not force:
            die(
                f"ya existe {target}\n"
                "  Usa --force para reemplazarlo, o bórralo a mano."
            )
        info(f"eliminando {target} (--force)")
        if not dry_run:
            shutil.rmtree(target)

    info(f"copiando {pack} → {target}")
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(pack, target)


def wire_agents_md(project_root: Path, *, dry_run: bool) -> None:
    agents = project_root / "AGENTS.md"
    if agents.is_file():
        try:
            text = agents.read_text(encoding="utf-8")
        except OSError as exc:
            die(f"no pude leer {agents}: {exc}")
        if SNIPPET_MARKER in text:
            info(f"AGENTS.md: marcador '{SNIPPET_MARKER}' ya presente, no se toca")
            return
        new_text = text.rstrip() + "\n\n" + SNIPPET
        action = "añadiendo snippet a"
    else:
        new_text = SNIPPET
        action = "creando"

    info(f"{action} {agents}")
    if not dry_run:
        try:
            agents.write_text(new_text, encoding="utf-8")
        except OSError as exc:
            die(f"no pude escribir {agents}: {exc}")


def verify(project_root: Path) -> None:
    """Comprobaciones alineadas con INSTALL (sin listar piezas fijas)."""
    pack = project_root / "docs" / "setup-roy"
    index = pack / "agents.md"
    agents_md = project_root / "AGENTS.md"
    problems: list[str] = []

    if not pack.is_dir():
        problems.append(f"falta el directorio del pack: {pack}")
    else:
        entries = [p for p in pack.iterdir() if p.name != ".git"]
        if not entries:
            problems.append(f"el pack está vacío: {pack}")
        if not index.is_file():
            problems.append(f"falta el índice: {index}")
        # Señal mínima de pack real (sin acoplar a skills/ concreto)
        has_substance = index.is_file() and (
            (pack / "EXTENDING.md").is_file()
            or any(p.is_dir() for p in entries)
        )
        if index.is_file() and not has_substance:
            problems.append(
                f"{pack} solo tiene archivos sueltos sin EXTENDING.md ni subcarpetas; "
                "no parece un pack setup-roy completo"
            )

    if not agents_md.is_file():
        problems.append(f"falta {agents_md}")
    else:
        try:
            text = agents_md.read_text(encoding="utf-8")
        except OSError as exc:
            problems.append(f"no pude leer {agents_md}: {exc}")
        else:
            count = text.count(SNIPPET_MARKER)
            if count == 0:
                problems.append(
                    f"{agents_md} no contiene el marcador '{SNIPPET_MARKER}'"
                )
            elif count > 1:
                problems.append(
                    f"{agents_md} tiene el marcador '{SNIPPET_MARKER}' {count} veces "
                    "(debería aparecer una sola vez)"
                )

    if problems:
        die(
            "la verificación falló:\n"
            + "\n".join(f"  - {p}" for p in problems)
        )

    info(f"ok: {index}")
    info(f"ok: marcador en {agents_md}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Instala setup-roy en un proyecto: copia el pack a docs/setup-roy/ "
            "y asegura el marcador en AGENTS.md."
        )
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument(
        "--from",
        dest="from_path",
        type=Path,
        help="Ruta local al repo setup-ia o a la carpeta setup-roy/",
    )
    src.add_argument(
        "--repo",
        help="URL git de setup-ia (clona en temporal y copia solo setup-roy/)",
    )
    p.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
        help="Raíz del proyecto destino (por defecto: directorio actual)",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Reemplaza docs/setup-roy/ si ya existe",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra qué haría sin escribir nada",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    project = args.project.resolve()
    if not project.exists():
        die(f"no existe el proyecto destino: {project}")
    if not project.is_dir():
        die(f"el proyecto destino no es un directorio: {project}")

    target = project / "docs" / "setup-roy"
    tmp: Path | None = None

    if args.dry_run:
        info("(dry-run: no se escribirá nada)")

    try:
        if args.from_path is not None:
            pack = find_pack_root(args.from_path)
            info(f"origen local: {pack}")
        else:
            assert args.repo is not None
            tmp = Path(tempfile.mkdtemp(prefix="setup-roy-"))
            pack = clone_repo(args.repo, tmp)
            info(f"origen clonado: {pack}")

        copy_pack(pack, target, force=args.force, dry_run=args.dry_run)
        wire_agents_md(project, dry_run=args.dry_run)
        if not args.dry_run:
            verify(project)
        info("listo.")
    finally:
        if tmp is not None and tmp.exists():
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
