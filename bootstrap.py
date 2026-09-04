#!/usr/bin/env python3
"""Install setup-roy into the current project (human or AI).

Copies only setup-roy/ → docs/setup-roy/ and wires the root AGENTS.md snippet.
Does not copy README, INSTALL, EXTENDING, or this script into the project.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SNIPPET = """## Setup Roy
Si la petición puede cubrirse con el pack en `docs/setup-roy/`, lee primero `docs/setup-roy/agents.md` y sigue su índice. Si no, trabaja con normalidad.
"""

SNIPPET_MARKER = "## Setup Roy"


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def find_pack_root(source: Path) -> Path:
    """Accept either the repo root or the setup-roy directory itself."""
    source = source.resolve()
    if (source / "setup-roy" / "agents.md").is_file():
        return source / "setup-roy"
    if (source / "agents.md").is_file() and source.name == "setup-roy":
        return source
    die(f"no setup-roy pack found under {source}")


def clone_repo(repo: str, dest: Path) -> Path:
    """Sparse-ish clone: full clone into temp then use setup-roy only."""
    print(f"cloning {repo} …")
    result = subprocess.run(
        ["git", "clone", "--depth", "1", repo, str(dest)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        die(f"git clone failed:\n{result.stderr.strip()}")
    return find_pack_root(dest)


def copy_pack(pack: Path, target: Path, *, force: bool, dry_run: bool) -> None:
    if target.exists():
        if not force:
            die(
                f"{target} already exists (use --force to replace, "
                "or remove it manually)"
            )
        print(f"removing existing {target}")
        if not dry_run:
            shutil.rmtree(target)

    print(f"copying {pack} → {target}")
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(pack, target)


def wire_agents_md(project_root: Path, *, dry_run: bool) -> None:
    agents = project_root / "AGENTS.md"
    if agents.is_file():
        text = agents.read_text(encoding="utf-8")
        if SNIPPET_MARKER in text:
            print(f"{agents}: snippet already present, skipping")
            return
        new_text = text.rstrip() + "\n\n" + SNIPPET
        action = "append"
    else:
        new_text = SNIPPET
        action = "create"

    print(f"{action} snippet in {agents}")
    if not dry_run:
        agents.write_text(new_text, encoding="utf-8")


def verify(project_root: Path) -> None:
    agents = project_root / "docs" / "setup-roy" / "agents.md"
    if not agents.is_file():
        die(f"verification failed: missing {agents}")
    print(f"ok: {agents}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Install setup-roy into the current project."
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument(
        "--from",
        dest="from_path",
        type=Path,
        help="Path to local setup-ia repo (or to setup-roy/)",
    )
    src.add_argument(
        "--repo",
        help="Git URL of setup-ia (clones temporarily, copies only setup-roy/)",
    )
    p.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
        help="Project root to install into (default: cwd)",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Replace existing docs/setup-roy/",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    project = args.project.resolve()
    if not project.is_dir():
        die(f"project root is not a directory: {project}")

    target = project / "docs" / "setup-roy"
    tmp: Path | None = None

    try:
        if args.from_path is not None:
            pack = find_pack_root(args.from_path)
        else:
            tmp = Path(tempfile.mkdtemp(prefix="setup-roy-"))
            pack = clone_repo(args.repo, tmp)

        copy_pack(pack, target, force=args.force, dry_run=args.dry_run)
        wire_agents_md(project, dry_run=args.dry_run)
        if not args.dry_run:
            verify(project)
        print("done.")
    finally:
        if tmp is not None and tmp.exists():
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
