# Extender setup-roy

Convenciones para añadir piezas al pack sin romper el diseño. Todo lo nuevo va **dentro** de `setup-roy/` y debe registrarse en `setup-roy/agents.md`.

## Dónde va cada cosa

| Tipo | Carpeta | Activación |
|------|---------|------------|
| Skill (disciplina / flujo) | `setup-roy/skills/<nombre>/` | Bajo demanda (el usuario la pide) |
| Agente especializado | `setup-roy/agents/<nombre>.md` | Bajo demanda; usable **solo**, sin orquestador |
| Orquestador | `setup-roy/orchestrator/` | Bajo demanda; solo cuando hace falta coordinar varios agentes |
| Script mecánico | `setup-roy/scripts/` | La IA o el humano lo ejecutan; no gastar tokens en lo que el script ya hace |

Docs de este repositorio (`README.md`, `INSTALL.md`, este archivo, `bootstrap.py`) **no** se copian a los proyectos.

## Checklist al añadir algo

1. Créalo en la carpeta correcta.
2. Añade una entrada en `setup-roy/agents.md` (índice): qué es y cuándo usarlo.
3. Si es un agente y el orquestador debe poder delegarle trabajo, actualiza también `setup-roy/orchestrator/orchestrator.md`.
4. Skills y agentes: dejan claro que **no** se activan solos salvo que el usuario lo pida.
5. Scripts:
   - CLI clara (`--help`).
   - `--dry-run` si tocan disco, git o red.
   - Sin secretos en el pack (claves SSH, tokens, passwords se resuelven en runtime).

## Ejemplo: añadir un agente usable solo

1. Crea `setup-roy/agents/debugger.md` con rol, límites y criterios de éxito.
2. En `setup-roy/agents.md`, añade algo como: *`agents/debugger.md` — bajo demanda para bugs difíciles.*
3. (Opcional) En `orchestrator/orchestrator.md`, menciónalo en la lista de agentes disponibles.

No hace falta meter el agente dentro de `orchestrator/`: vive en `agents/` y se invoca directo (*“usa el agente debugger”*).

## Ejemplo: añadir un script

1. Crea `setup-roy/scripts/mi_tool.py` con argparse y `--dry-run` si aplica.
2. Documenta el uso en `setup-roy/scripts/README.md`.
3. Regístralo en `setup-roy/agents.md`.

## Naming

- Skills: carpeta en kebab-case con `SKILL.md` dentro (`skills/grilling/SKILL.md`).
- Agentes: un `.md` por agente en `agents/` (`reviewer.md`).
- Scripts: `snake_case.py`.
