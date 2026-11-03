---
name: sdd
description: >
  Spec-Driven Development: deliver one clearly scoped product change through a
  full specification workflow: brief, clarification, technical plan,
  requirements review, tasks, cross-check, implementation, and final review.
  Supports auto (default; proceeds with stated assumptions) and pausas (stops
  for decisions only the user can make). Use when the user asks for SDD,
  spec-driven development, or a full specification workflow.
argument-hint: "[auto|pausas]"
---

# SDD — Spec-Driven Development

Deliver one clearly scoped product change in this project through a specification-led workflow, then stop. Treat each request as a separate task.

**Level** (for this request only): `auto` (default) or `pausas`. Use `auto` to proceed without pausing for product decisions, recording assumptions in the closeout. Use `pausas` or `guided` to stop for decisions only the user can make.

## Hard rules

1. **One shot** — Complete the requested change, or clearly report what blocks it. Treat later requests as separate tasks.
2. **Repo anchor first** — Analyze the request and relevant project context, including `AGENTS.md`, docs, nearby code, conventions, constraints, and risks.
3. **Keep moving** — In `auto`, complete the phases and implement without pausing for product decisions. State assumptions in the closeout.
4. **`pausas` decisions** — Write no code until the user answers the numbered decision questions. Then continue in the same thread; pause again only if cross-check reveals a new decision only the user can make.
5. **Keep scope local** — Avoid project-wide rules or configuration unless asked. Update existing docs when the change makes them inaccurate; do not create docs when none are relevant.
6. **Complete the change** — Use the phases to guide the work; do not stop after producing the specification or plan when implementation is expected.
7. **Checks** — Skip tests by default. Run them only if requested or a quick check is necessary; report results accurately.
8. **Respect Git boundaries** — Do not commit or push unless explicitly asked.

## Pipeline (always, in order)

The phase names align with Spec Kit ideas. Do not require `/speckit-*` commands or `.specify/` unless the project already uses them.

| Step | Name | Do |
|------|------|-----|
| 0 | **Repo anchor** | Analyze the request and relevant project context; identify the goal, constraints, patterns, and risks. |
| 1 | **Brief** (`specify`) | Define the problem, desired outcome, acceptance criteria, and scope. Keep it in product language; defer stack details to step 3. |
| 2 | **Clarify** (`clarify`) | Surface gaps, edge cases, and assumptions. In `pausas`, identify decisions only the user can make. |
| — | **Pause 1** | In `pausas`, if the user must decide a product behavior, provide credentials, or accept an irreversible tradeoff, list numbered **Decisions**, each with a recommendation, then stop without writing code. Otherwise continue. |
| 3 | **Technical Plan** (`plan`) | Decide how and where to implement the change in this codebase, including relevant modules, files, data, and dependencies. |
| 4 | **Requirements Review** (`checklist`) | Check that the brief is complete and implementable without guessing; resolve gaps before creating tasks. |
| 5 | **Tasks** (`tasks`) | Break the plan into concrete, ordered tasks. Each task should advance a brief requirement and have a clear completion check; omit filler tasks. |
| 6 | **Cross-check** (`analyze`) | Check that the brief, plan, and tasks agree. In `auto`, resolve inconsistencies and proceed. In `pausas`, pause only if the conflict requires a decision only the user can make; otherwise resolve it and continue. |
| 7 | **Implement** (`implement`) | Complete the tasks using the project’s conventions. |
| 8 | **Converge** (`converge`) | Check the result against the brief and tasks, report checks run, and note any configuration or secrets the user must provide. In `auto`, briefly list important assumptions. |

### When to pause (`pausas` only)

Pause without writing code only for decisions that cannot be resolved from the repo or safe defaults, such as business rules, credentials, choosing between valid product behaviors, or conflicting scope. Do not pause for style, file paths, or fixable inconsistencies; resolve those and continue.

## Response shape

Keep the preamble compact, then do the work.

**`auto` or after the user answers in `pausas`:**

```markdown
## SDD · <piece title>
**Done when:** …
**Out of scope:** …
**Assumptions:** … (required in auto; optional in pausas if already agreed)
**Task plan:** 1) … 2) …
---
(implementation and verification note)
```

**`pausas` waiting on user:**

```markdown
## SDD · <piece title> — decisions
Reply with a number or a short phrase. Implementation is paused until you answer.

1. **<title>:** …
   → Recommended: …
```

## If Spec Kit files exist

Update `spec.md`, `plan.md`, or `tasks.md` in the project’s Spec Kit layout only when that is already the team workflow. Otherwise, keep the brief in the chat or at a path the user named. Do not run `specify init` unless asked.
