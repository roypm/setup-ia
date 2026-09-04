# setup-ia

**setup-roy** — Kit mínimo reutilizable para trabajar con IA en cualquier proyecto (nuevo o ya empezado).

Lo que viaja a tus repos es solo la carpeta **`setup-roy/`**. El resto de este repositorio documenta cómo instalarlo y cómo extenderlo.

## Qué hay dentro

| Ruta | ¿Se copia al proyecto? | Para qué |
|------|------------------------|----------|
| [`setup-roy/`](setup-roy/) | **Sí** → `docs/setup-roy/` | Skills, agentes, orquestador, scripts, guía de extensión |
| [`INSTALL.md`](INSTALL.md) | No | Cómo instalar (humano e IA) |
| [`bootstrap.py`](bootstrap.py) | No | Instala el pack y actualiza `AGENTS.md` |

Cómo instalar: **[INSTALL.md](INSTALL.md)**.  
Cómo añadir piezas al pack: **[`setup-roy/EXTENDING.md`](setup-roy/EXTENDING.md)** (viaja con el pack a cada proyecto).

## Resultado en un proyecto

Así queda en tu repo (se crea `docs/` o `AGENTS.md` si no existen):

```text
tu-proyecto/
├── AGENTS.md              ← snippet que apunta al pack
└── docs/
    └── setup-roy/
        ├── agents.md      ← índice (entrada)
        ├── EXTENDING.md   ← cómo añadir piezas
        ├── skills/
        ├── agents/
        ├── orchestrator/
        └── scripts/
```

## Cómo se usa

Cuando pides algo que cubre el pack, la IA entra por el `AGENTS.md` de la raíz. Ahí está el snippet que la redirige a `docs/setup-roy/agents.md`, donde se decide qué pieza usar según la tarea y cómo debe actuar cada una. Si la tarea no está cubierta por el pack, trabaja con normalidad.
