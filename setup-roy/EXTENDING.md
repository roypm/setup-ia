# Extending this pack

Guide for **adding pieces** to setup-roy without breaking the design. Applies in the meta-repo (`setup-ia`) and in a project where the pack lives at `docs/setup-roy/`.

The index [`agents.md`](agents.md) is the source of truth: if it is not registered there, for the AI it **does not exist**.

**Language:** base pack docs ship in English (faster for models). New pieces may be written in another language if the index entry is clear about when to use them.

## Principles

1. **On demand:** skills, agents, orchestrators, and similar activate only when the user asks (or the orchestrator delegates).
2. **Stable router:** you do not need to change the project-root `AGENTS.md` snippet when adding pieces; evolve this pack and its index.
3. **One piece, one place:** do not duplicate the same logic across skill + agent + workflow doc.
4. **No secrets** in the pack (tokens, keys, passwords are resolved at runtime).

## Where things go

Paths relative to this pack root (`setup-roy/` or `docs/setup-roy/`):

| Type | Typical folder | Notes |
|------|----------------|-------|
| Skill (discipline / flow) | `skills/<name>/` | Usually includes `SKILL.md` |
| Specialized agent | `agents/<name>.md` | Usable alone, without orchestrator |
| Orchestrator / flows | `orchestrator/` | Coordinates agents; named flows in `orchestrator.md` |
| Workflow policy | `workflows/` | Shared conventions (e.g. git-flow); not an agent |
| Mechanical script | `scripts/` | Optional CLI; do not burn tokens on what a script already does |
| Templates / prompts | `prompts/` or `templates/` | PR, issues, messages; register in the index |
| Checklists | `checklists/` (or similar) | Definition of done, pre-merge, etc. |
| MCP / IDE config | see [MCP and IDE](#mcp-and-ide) | Often environment config, not only a `.md` |
| New type | Propose a folder here | Same [common checklist](#common-checklist) + index entry |

If unsure of the type: **index first** (clear entry) and a folder that does not collide with existing ones.

## Common checklist

Regardless of piece type:

1. Create it in the right folder (or propose a new one with a clear reason).
2. Add an entry in [`agents.md`](agents.md): what it is, when to use it, path.
3. State on-demand activation explicitly (except scripts the user/AI runs on purpose).
4. If an orchestrator should be able to delegate to it, update `orchestrator/` (agent list / flow).
5. Do not put secrets or meta-repo install files (`INSTALL.md`, `bootstrap.py`, etc.) into the pack.
6. Do not change the project-root canonical snippet unless the **router contract** itself changes (rare).

### Extra for scripts

- Clear CLI (`--help`).
- `--dry-run` if it touches disk, git, or the network.
- Brief usage in `scripts/README.md` (or equivalent) **and** in the index.

### Extra for skills or agents

- Role, limits (what it does not do), and success criteria.
- Agents: one `.md` per agent under `agents/`.

### Extra for workflows

- Short policy doc; agents and orchestrator link to it instead of re-stating rules.
- Register in [`agents.md`](agents.md).

## MCP and IDE

MCP servers, Cursor/Claude rules, or other tool configs:

- May live as **docs + examples** in the pack (e.g. `mcp/`) or as guidance to apply in the destination project.
- Register them in [`agents.md`](agents.md) (when to use / what they add).
- Do not assume every consumer uses the same IDE: the index must work without MCP.
- Credentials and private URLs: outside the versioned pack.

## Naming

- Skills: kebab-case folder with `SKILL.md` (`skills/grilling/SKILL.md`).
- Agents: short-name file in `agents/` (`surgical.md`).
- Scripts: `snake_case.py` (if you add any).
- Orchestrators: clear markdown under `orchestrator/` (`orchestrator.md`).
- Workflows: kebab-case under `workflows/` (`git-flow.md`).

## Examples

### Standalone agent

1. Create `agents/security.md` (role, limits, success).
2. In `agents.md`: when to use it and the path.
3. Mention it in [`orchestrator/orchestrator.md`](orchestrator/orchestrator.md) if it should be delegable in a named flow.

Do not put it inside `orchestrator/`: it lives in `agents/` and is invoked directly.

### Workflow policy

1. Create `workflows/release-notes.md` (or similar).
2. Entry in `agents.md`: *when to follow this policy*.
3. Link from the orchestrator `ship` (or other) flow if relevant.

### New type (e.g. templates)

1. Create `prompts/pr_body.md` (or the folder you choose).
2. Entry in `agents.md`: *when to use this template*.
3. No need to touch the project-root `AGENTS.md` snippet.

## What you usually do not need to touch

- Meta-repo install (`INSTALL.md`, `bootstrap.py`) — unless how the pack is installed changes.
- Project-root `AGENTS.md` snippet — new catalog entries are discovered via this index after updating the pack.
- Meta-repo README — only if you want to announce the piece to humans.
