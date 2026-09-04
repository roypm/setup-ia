# setup-ia

**setup-roy** — Kit mínimo reutilizable para trabajar con IA en cualquier proyecto (nuevo o ya empezado).

Lo que viaja a tus repos es solo la carpeta **`setup-roy/`**. El resto de este repositorio documenta cómo instalarlo y cómo extenderlo.

## Qué hay dentro

| Ruta | ¿Se copia al proyecto? | Para qué |
|------|------------------------|----------|
| [`setup-roy/`](setup-roy/) | **Sí** → `docs/setup-roy/` | Skills, agentes, orquestador, workflows, guía de extensión |
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
        └── workflows/
```

## Cómo se usa

Cuando pides algo que cubre el pack, la IA entra por el `AGENTS.md` de la raíz. El snippet la redirige a `docs/setup-roy/agents.md` (índice en inglés): allí elige la pieza según la tarea. Si no encaja con el pack, trabaja con normalidad. El contenido base del pack está en inglés para las IAs; puedes añadir piezas nuevas en otro idioma si el índice queda claro.
