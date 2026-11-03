---
name: ftd
description: >
  Fast Track Development: implement one clearly scoped feature or
  product change in the current repo with a lightweight workflow. Understand
  the existing code, define the outcome briefly, plan the implementation,
  make the change, and summarize what was done and checked. Use when the user
  asks for FTD, fast-track development, or lightweight implementation.
---

# FTD — Fast Track Development

Implement one clearly scoped feature or product change with a lightweight, end-to-end workflow. Understand the relevant code, define the outcome briefly, plan and implement the change, then summarize what was done and checked. Treat each request as a separate task and stop when it is complete.

## Hard rules

1. **Start with the repo** — Read the relevant files and follow the project’s existing patterns.
2. **Keep moving** — If missing information blocks part of the work, state what is missing and continue with the parts that do not depend on it. If nothing can be done safely, stop and ask for that information.
3. **Keep scope local** — Avoid project-wide rules or configuration unless asked. Update existing docs when the change makes them inaccurate; don’t create docs when none are relevant.
4. **Complete the change** — Use the brief and plan to guide implementation; do not stop after writing them.
5. **Checks** — Skip tests by default. Run them only if requested or a quick check is necessary; report results accurately.
6. **Respect Git boundaries** — Do not commit or push unless explicitly asked.

## Pipeline (in order)

| Step | Name | Do |
|------|------|-----|
| 0 | **Repo anchor** | Analyze the request and relevant code; identify the goal, constraints, project patterns, and risks. |
| 1 | **Brief** (`specify`) | Summarize what will change, what is out of scope, and how to tell when it is done. |
| 2 | **Technical Plan** (`plan`) | Decide where and how to make the change in this codebase. |
| 3 | **Tasks** (`tasks`) | Break the plan into concrete, ordered tasks. Each task should advance a brief requirement and have a clear completion check; omit filler tasks. |
| 4 | **Implement** (`implement`) | Apply the changes. |
| 5 | **Converge** (`converge`) | Check whether the brief was met, report checks run, and state any assumptions briefly. |

## Response shape (optional, keep short)

```markdown
## FTD · <piece title>
**Done when:** …
**Tasks:** 1) …
---
(implementation + verification note)
```

Scale the plan and tasks to the size of the change without adding unnecessary phases.
