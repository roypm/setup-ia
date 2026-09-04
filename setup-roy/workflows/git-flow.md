# Git flow (main / develop / PR)

Policy for this pack. Not an agent — agents and the orchestrator follow it when branching, committing, or shipping.

## Branches

| Branch | Role |
|--------|------|
| `main` | Production. Deploy from here. |
| `develop` | Integration. Daily work lands here. |

Feature work may use `feature/*` (or similar) and merge into `develop` first.

## Daily work

1. Commit on `develop` or on a feature branch that merges to `develop`.
2. Do **not** commit directly to `main` unless the user explicitly demands an emergency exception.
3. Commits and pushes only when the user asks.

## Release

1. When `develop` is ready, open a PR: **develop → main**.
2. Do not merge that PR blindly; wait for review/CI as the user expects.
3. After merge to `main`, production deploy runs (typically GitHub Actions on `main`).

## Deploy

- Prefer **deploy from `main`** (push or merge of the release PR).
- Do **not** deploy from every commit on `develop` by default.

## Bootstrap

If `develop` does not exist yet: create it once from `main` and push with tracking when the user wants that setup.

## Safety

- Never `--force` push to `main` or `develop` unless the user explicitly asks.
- Never skip hooks (`--no-verify`, etc.) unless explicitly asked.
- Do not rewrite shared history casually.
