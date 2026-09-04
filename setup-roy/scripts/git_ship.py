#!/usr/bin/env python3
"""Commit and push with interactive SSH key + author selection.

Designed so the AI only supplies the message (and optional paths); identity and
SSH are handled here without burning tokens on git plumbing.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

SSH_DIR = Path.home() / ".ssh"
SKIP_KEY_NAMES = {
    "authorized_keys",
    "config",
    "known_hosts",
    "known_hosts.old",
}


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def run_checked(
    cmd: list[str],
    *,
    env: dict[str, str] | None = None,
    dry_run: bool = False,
) -> str:
    print("+", " ".join(cmd))
    if dry_run:
        return ""
    result = subprocess.run(cmd, env=env, text=True, capture_output=True)
    if result.returncode != 0:
        err = (result.stderr or result.stdout or "").strip()
        die(f"command failed ({result.returncode}): {' '.join(cmd)}\n{err}")
    return (result.stdout or "").strip()


def git_config(key: str) -> str | None:
    result = subprocess.run(
        ["git", "config", "--get", key],
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    value = (result.stdout or "").strip()
    return value or None


def list_ssh_private_keys(ssh_dir: Path = SSH_DIR) -> list[Path]:
    if not ssh_dir.is_dir():
        return []
    keys: list[Path] = []
    for path in sorted(ssh_dir.iterdir()):
        if not path.is_file():
            continue
        name = path.name
        if name.startswith("."):
            continue
        if name.endswith(".pub"):
            continue
        if name in SKIP_KEY_NAMES:
            continue
        # Heuristic: treat as private key if a matching .pub exists, or
        # common key name prefixes.
        pub = path.with_name(path.name + ".pub")
        if pub.is_file() or name.startswith(("id_", "ssh_")):
            keys.append(path)
    return keys


def prompt_choice(title: str, options: list[str], default_index: int = 0) -> int:
    print(title)
    for i, opt in enumerate(options, start=1):
        mark = " (default)" if i - 1 == default_index else ""
        print(f"  {i}) {opt}{mark}")
    while True:
        raw = input(f"choose [1-{len(options)}] (Enter={default_index + 1}): ").strip()
        if raw == "":
            return default_index
        if raw.isdigit():
            n = int(raw)
            if 1 <= n <= len(options):
                return n - 1
        print("invalid option")


def prompt_text(label: str, default: str | None) -> str:
    suffix = f" [{default}]" if default else ""
    raw = input(f"{label}{suffix}: ").strip()
    if raw:
        return raw
    if default:
        return default
    die(f"{label} is required")


def select_key(explicit: str | None, *, non_interactive: bool) -> Path | None:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if not path.is_file():
            die(f"SSH key not found: {path}")
        return path

    keys = list_ssh_private_keys()
    if not keys:
        print("warning: no SSH private keys found under ~/.ssh; push may use default agent")
        return None

    if len(keys) == 1:
        print(f"SSH key: {keys[0]} (only key found)")
        return keys[0]

    if non_interactive:
        die(
            "multiple SSH keys found; pass --key <path> "
            "or run interactively"
        )

    labels = [str(k) for k in keys]
    idx = prompt_choice("SSH keys found:", labels, 0)
    return keys[idx]


def select_author(
    name: str | None,
    email: str | None,
    *,
    non_interactive: bool,
) -> tuple[str, str]:
    default_name = name or git_config("user.name")
    default_email = email or git_config("user.email")

    if name and email:
        return name, email

    if non_interactive:
        if not default_name or not default_email:
            die(
                "missing user.name / user.email; pass --name and --email "
                "or configure git"
            )
        return default_name, default_email

    print("Commit author (Enter = default):")
    final_name = prompt_text("  name", default_name)
    final_email = prompt_text("  email", default_email)
    return final_name, final_email

def build_env(key: Path | None) -> dict[str, str]:
    env = os.environ.copy()
    if key is not None:
        # IdentitiesOnly avoids falling back to other keys silently.
        env["GIT_SSH_COMMAND"] = (
            f"ssh -i {key} -o IdentitiesOnly=yes"
        )
    return env


def ensure_git_repo() -> None:
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        die("not inside a git work tree")


def stage_paths(paths: list[str], *, dry_run: bool) -> None:
    if not paths:
        return
    run_checked(["git", "add", "--", *paths], dry_run=dry_run)


def has_staged_changes() -> bool:
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        capture_output=True,
    )
    # exit 1 => differences (staged changes present)
    return result.returncode == 1


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Commit and push with SSH key + author selection."
    )
    p.add_argument(
        "-m",
        "--message",
        required=True,
        help="Commit message",
    )
    p.add_argument(
        "--key",
        help="Path to SSH private key (skip interactive pick)",
    )
    p.add_argument("--name", help="Commit author name")
    p.add_argument("--email", help="Commit author email")
    p.add_argument(
        "--no-push",
        action="store_true",
        help="Commit only, do not push",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without mutating git",
    )
    p.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Non-interactive: require --key if multiple keys; use git config for author",
    )
    p.add_argument(
        "paths",
        nargs="*",
        help="Optional paths to git add before commit",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    ensure_git_repo()

    key = select_key(args.key, non_interactive=args.yes)
    author_name, author_email = select_author(
        args.name, args.email, non_interactive=args.yes
    )

    print(f"author: {author_name} <{author_email}>")
    if key:
        print(f"ssh:    {key}")

    if args.paths:
        stage_paths(args.paths, dry_run=args.dry_run)
    elif not args.dry_run and not has_staged_changes():
        die("nothing staged; pass paths to add, or git add first")
    elif args.dry_run and not args.paths:
        print("(dry-run) skipping staged-changes check")

    env = build_env(key)
    # Force author for this commit only.
    env["GIT_AUTHOR_NAME"] = author_name
    env["GIT_AUTHOR_EMAIL"] = author_email
    env["GIT_COMMITTER_NAME"] = author_name
    env["GIT_COMMITTER_EMAIL"] = author_email

    run_checked(
        ["git", "commit", "-m", args.message],
        env=env,
        dry_run=args.dry_run,
    )

    if args.no_push:
        print("skip push (--no-push)")
        print("done.")
        return

    # Push current branch to its upstream, or -u origin HEAD if none.
    branch = run_checked(["git", "rev-parse", "--abbrev-ref", "HEAD"], dry_run=False)
    upstream = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
        capture_output=True,
        text=True,
    )
    if upstream.returncode == 0:
        run_checked(["git", "push"], env=env, dry_run=args.dry_run)
    else:
        run_checked(
            ["git", "push", "-u", "origin", branch],
            env=env,
            dry_run=args.dry_run,
        )
    print("done.")


if __name__ == "__main__":
    main()
