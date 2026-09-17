# Offer gate

Shared policy: when a **mode** piece of this pack clearly fits the user’s request, offer it in **one line** and wait. Do not silently enter that mode.

Not an agent. Index, agents, and skills follow this when a piece below would change *how* the work is done.

## When to run

After reading [`../agents.md`](../agents.md), before activating an offerable piece by inference (user did not name it).

## Offerable pieces (only these)

| Priority (high → low) | Piece | Offer when (signals) |
|----------------------|--------|----------------------|
| 1 | [`companion`](../agents/companion.md) | Guide me / step by step / learn-by-doing / “I want to do X” myself |
| 2 | [`grilling`](../skills/grilling/SKILL.md) | Open decision, ambiguous design, “help me decide”, stress-test a plan |
| 3 | [`ponytail`](../skills/ponytail/SKILL.md) | Minimal / YAGNI / anti-overengineering / “do less” |
| 4 | [`security`](../agents/security.md) | Harden, secrets/PII, auth/routes/DB sealing before prod |
| 5 | [`tester`](../agents/tester.md) | Add or strengthen real tests for a change |
| 6 | [`actions`](../agents/actions.md) | GitHub Actions / CI/CD workflows |
| 7 | [`i18n`](../agents/i18n.md) | Locales, new user-facing strings, translation |

**Never offer via this gate:** `coder`, `surgical`, `orchestrator`, `git-flow` — use normal routing / user ask / orchestrator delegation instead.

## Offer format

Exactly **one line**, then stop that turn (no implementation, no protocol start):

- Piece **name in English** (as in the index).
- Micro-reason ≤ **6 words** in the **user’s language**.
- Clear `(sí / no)` or `(yes / no)` matching the user’s language.

Example (user in Spanish):

`¿Usamos **companion** del pack para guiarte paso a paso? (sí / no)`

Example (user in English):

`Use **grilling** from the pack to close this decision? (yes / no)`

## Selection rules

1. If **zero** clear matches → do not offer; work normally.
2. If **two or more** match → offer **only** the highest-priority one in the table above.
3. At most **one** offer per user message.
4. If the user already **named** the piece, or that protocol is **already active** → do not offer; follow that piece.
5. **Skip offer** when: trivial request (e.g. rename one symbol); low confidence; or user asked to **implement now** / “hazlo tú” / “just do it” — in that last case do **not** offer companion, grilling, or ponytail.
6. Clear **yes** → open that piece’s file and follow it.
7. Anything that is not a clear yes (**no**, ignore, new unrelated ask, paste-and-“do this”) → treat as **no**: fulfill the request **without** that mode; do **not** re-offer that piece for this work thread.

## Anti-patterns

- Multi-line sales pitch or listing several pieces
- Offering coder/surgical “just in case”
- Starting the piece’s protocol in the same turn as the offer
- Re-asking after a no or a silent continue
