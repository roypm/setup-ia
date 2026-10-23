# setup-ia

**setup-roy** — Kit mínimo reutilizable para trabajar con IA en cualquier proyecto (nuevo o ya empezado).

Lo que viaja a tus repos es solo la carpeta **`setup-roy/`**. El resto de este repositorio documenta cómo instalarlo.

## Qué hay dentro

| Ruta | ¿Se copia al proyecto? | Para qué |
|------|------------------------|----------|
| [`setup-roy/`](setup-roy/) | **Sí** → `docs/setup-roy/` | Skills y agentes |
| [`INSTALL.md`](INSTALL.md) | No | Contrato de instalación (IA) |

La instalación es **solo por IA**: no hay script. En el proyecto donde quieras el pack, abre el chat del agente y pega este mensaje:

```text
Instala setup-roy en este proyecto. Sigue https://github.com/roypm/setup-ia/blob/main/INSTALL.md (pregunta si quieres todo o piezas; si es a medida, lista cada herramienta con su objetivo).
```

Contrato detallado: **[INSTALL.md](INSTALL.md)**.

## Resultado en un proyecto

Así queda en tu repo (se crea `docs/` o `AGENTS.md` si no existen):

```text
tu-proyecto/
├── AGENTS.md              ← snippet que apunta al pack
└── docs/
    └── setup-roy/
        ├── agents.md      ← qué es el pack en este proyecto
        ├── skills/
        └── agents/
```

## Cómo se usa

Cuando el trabajo encaja con el pack, la IA lee `docs/setup-roy/agents.md` y abre la pieza que toque bajo ese árbol. Si no encaja, ignora el pack. El contenido base del pack está en inglés para las IAs.
