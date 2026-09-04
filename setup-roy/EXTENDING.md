# Extender este pack

Guía para **añadir piezas** a setup-roy sin romper el diseño. Válida tanto en el meta-repo (`setup-ia`) como en un proyecto donde el pack ya está en `docs/setup-roy/`.

El índice [`agents.md`](agents.md) es la fuente de verdad: si no está registrado ahí, para la IA **no existe**.

## Principios

1. **Bajo demanda:** skills, agentes, orquestadores y similares solo se activan cuando el usuario lo pide (o el orquestador delega).
2. **Router estable:** el snippet de `AGENTS.md` en la raíz del proyecto no hace falta tocarlo al añadir piezas; evoluciona este pack y su índice.
3. **Una pieza, un sitio:** no dupliques la misma lógica en skill + agente + script.
4. **Sin secretos** en el pack (tokens, claves, passwords se resuelven en runtime).

## Dónde va cada cosa

Rutas relativas a la raíz de este pack (`setup-roy/` o `docs/setup-roy/`):

| Tipo | Carpeta típica | Notas |
|------|----------------|-------|
| Skill (disciplina / flujo) | `skills/<nombre>/` | Suele llevar `SKILL.md` |
| Agente especializado | `agents/<nombre>.md` | Usable solo, sin orquestador |
| Orquestador / flujos | `orchestrator/` | Coordina agentes; puede haber varios flujos |
| Script mecánico | `scripts/` | CLI; no gastar tokens en lo que el script ya hace |
| Plantillas / prompts | `prompts/` o `templates/` | PR, issues, mensajes; registrar en el índice |
| Checklists | `checklists/` (o similar) | Definition of done, pre-merge, etc. |
| MCP / config de IDE | ver [MCP e IDE](#mcp-e-ide) | A menudo es config del entorno, no solo un `.md` |
| Tipo nuevo | Propón carpeta aquí | Misma [checklist](#checklist-común) + entrada en el índice |

Si no estás seguro del tipo: **índice primero** (entrada clara) y carpeta que no choque con las existentes.

## Checklist común

Da igual el tipo de pieza:

1. Créala en la carpeta correcta (o propone una nueva con criterio).
2. Añade una entrada en [`agents.md`](agents.md): qué es, cuándo usarla, ruta.
3. Deja explícita la activación bajo demanda (salvo scripts que el usuario/IA ejecutan a propósito).
4. Si un orquestador debe poder delegarle trabajo, actualiza `orchestrator/` (lista de agentes / flujo).
5. No metas secretos ni archivos del meta-repo de instalación (`INSTALL.md`, `bootstrap.py`, etc.).
6. No cambies el snippet canónico de la raíz del proyecto salvo que cambie el **contrato del router** (raro).

### Extra si es script

- CLI clara (`--help`).
- `--dry-run` si toca disco, git o red.
- Documenta uso breve en `scripts/README.md` (o equivalente) **y** en el índice.

### Extra si es skill o agente

- Rol, límites (qué no hace) y criterio de éxito.
- Agentes: un `.md` por agente en `agents/`.

## MCP e IDE

MCP servers, rules de Cursor/Claude u otras configs de herramienta:

- Pueden vivir como **documentación + ejemplo** en el pack (p. ej. `mcp/`) o como guía “aplicar en el proyecto destino”.
- Regístralos en [`agents.md`](agents.md) (cuándo usarlos / qué aportan).
- No asumas que todos los consumidores usan el mismo IDE: el índice debe funcionar aunque no haya MCP.
- Credenciales y URLs privadas: fuera del pack versionado.

## Naming

- Skills: carpeta en kebab-case con `SKILL.md` (`skills/grilling/SKILL.md`).
- Agentes: un archivo de nombre corto en `agents/` (`reviewer.md`).
- Scripts: `snake_case.py`.
- Orquestadores: markdown claro en `orchestrator/` (`orchestrator.md`, o `flows/<nombre>.md` si hay varios).

## Ejemplos

### Agente usable solo

1. Crea `agents/debugger.md` (rol, límites, éxito).
2. En `agents.md`: cuándo usarlo y la ruta.
3. (Opcional) Menciónalo en el orquestador si debe poder delegarse.

No hace falta meterlo dentro de `orchestrator/`: vive en `agents/` y se invoca directo.

### Script

1. Crea `scripts/mi_tool.py` con argparse y `--dry-run` si aplica.
2. Documenta en `scripts/README.md`.
3. Regístralo en `agents.md`.

### Tipo nuevo (p. ej. plantillas)

1. Crea `prompts/pr_body.md` (o la carpeta que elijas).
2. Entrada en `agents.md`: *cuándo usar esta plantilla*.
3. No hace falta tocar el snippet de `AGENTS.md` en la raíz del proyecto.

## Qué no hace falta tocar al extender

- Instalación del meta-repo (`INSTALL.md`, `bootstrap.py`) — salvo que cambie la forma de instalar el pack.
- El snippet de `AGENTS.md` en la raíz del proyecto — el catálogo nuevo se descubre vía este índice tras actualizar el pack.
- README del meta-repo — solo si quieres anunciar la pieza a humanos.
