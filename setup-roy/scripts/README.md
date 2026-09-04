# Scripts (setup-roy)

Mechanical tools: the AI (or you) runs them; do not reinvent the flow in prompts.

## `git_ship.py`

Commit + push with SSH key and author selection.

```bash
# From the project root (after installing the pack):
python docs/setup-roy/scripts/git_ship.py -m "commit message"

# Add paths, skip push, dry-run:
python docs/setup-roy/scripts/git_ship.py -m "fix x" path/a path/b --no-push
python docs/setup-roy/scripts/git_ship.py -m "msg" --dry-run

# Non-interactive (CI / AI with choices already made):
python docs/setup-roy/scripts/git_ship.py -m "msg" --yes \
  --key ~/.ssh/id_ed25519_work \
  --name "Name" --email "you@email"
```

Behavior:

1. Lists private keys under `~/.ssh/` (heuristic: `id_*` / `ssh_*` or sibling `.pub`).
2. If several, asks which to use (or requires `--key` with `--yes`).
3. Proposes author from `git config user.*`; allows override.
4. `git commit` with that author; `GIT_SSH_COMMAND` with the chosen key.
5. `git push` to the branch upstream, or `git push -u origin <branch>` if none.

Flags: `-m/--message`, `--key`, `--name`, `--email`, `--no-push`, `--dry-run`, `-y/--yes`, and optional paths for `git add`.
