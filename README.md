# setup-ia

**setup-roy** — Kit mínimo reutilizable para trabajar con IA en cualquier proyecto (nuevo o ya empezado).

Lo que viaja a tus repos es solo la carpeta **`setup-roy/`**. El resto de este repositorio documenta cómo instalarlo.

## Qué hay dentro

| Ruta | ¿Se copia al proyecto? | Para qué |
|------|------------------------|----------|
| [`setup-roy/`](setup-roy/) | **Sí** → `docs/setup-roy/` | Skills y agentes |
| [`INSTALL.md`](INSTALL.md) | No | Contrato de instalación (IA) |

La instalación y la actualización son **solo por IA** (no hay script). En la raíz del proyecto, abre el chat y pega:

**Instalar** (proyecto sin pack o ampliación acordada):

```text
Instala setup-roy en este proyecto según https://github.com/roypm/setup-ia/blob/main/INSTALL.md
```

**Actualizar** (ya existe `docs/setup-roy/`):

```text
Actualiza setup-roy en este proyecto según https://github.com/roypm/setup-ia/blob/main/INSTALL.md
```

Qué te preguntará la IA: **[instalar](INSTALL.md#qué-verás-en-el-chat)** · **[actualizar](INSTALL.md#qué-verás-al-actualizar)**. Contrato completo: **[INSTALL.md](INSTALL.md)**.

En el proyecto destino quedan `AGENTS.md` (snippet) y `docs/setup-roy/` con el pack; el contenido concreto de cada versión lo describe `docs/setup-roy/agents.md` tras instalar.

## Cómo se usa

Cuando el trabajo encaja con el pack, la IA lee `docs/setup-roy/agents.md` y abre la pieza que toque bajo ese árbol. Si no encaja, ignora el pack. El contenido base del pack está en inglés para las IAs.
