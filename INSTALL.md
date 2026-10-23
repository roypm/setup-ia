# Instalar setup-roy

Instalación **solo por IA**: este archivo es el contrato. No hay script en el meta-repo; la IA obtiene el pack y lo deja en el proyecto destino.

## Resultado esperado

En la raíz del proyecto destino:

1. Existe `docs/setup-roy/` con **todo el pack** o **solo las piezas que eligió el usuario** (siempre incluye `agents.md`).
2. Existe `AGENTS.md` con el [snippet canónico](#snippet-canonico). Se crea el archivo si no existía; si ya tenía el snippet, no se duplica.

---

## Snippet canónico

Marcador: `## Setup Roy`. Si ya está en `AGENTS.md`, no lo dupliques. Si no está, añade este bloque en el `AGENTS.md` de la **raíz** del proyecto:

```markdown
## Setup Roy
Optional pack in `docs/setup-roy/`. When the user or the task points there, read `docs/setup-roy/agents.md` and follow whatever piece fits under that tree. Otherwise work normally.
```

---

## Contrato para la IA

Activa este contrato cuando el usuario pida instalar, configurar, actualizar o añadir **setup-roy** (o este repo) al proyecto actual.

### Diálogo con el usuario (obligatorio salvo atajos)

**Idioma:** habla con el usuario en su idioma. Los archivos que copies del pack **no** los traduzcas (el pack va en inglés para las IAs).

**Tono:** evita narrar pasos internos (“clonando…”, “consultando…”). Un resumen breve del inventario actual basta (p. ej. cuántos skills y agentes hay en esta versión).

**Interpretación flexible** (equivale a lo que dice el usuario):

| Intención | Acepta también (ejemplos) |
|-----------|---------------------------|
| **Todo** el pack | `completo`, `entero`, `full`, `all`, `todo el setup-roy` |
| **A medida** / piezas | `a media` (typo), `parcial`, `custom`, `solo algunas`, `piezas concretas` |
| **Atajo con piezas** | En el primer mensaje ya nombra ids o nombres (`solo sdd, ftd y coder`) |

1. **Obtén el pack** primero (clone o ZIP; ver [Procedimiento](#procedimiento)) para saber qué hay en la versión actual.
2. Si el usuario **ya pidió todo** (tabla anterior) → instala **todo** `setup-roy/` sin menú; opcional: una línea con el recuento (N skills, M agentes, workflows si hay).
3. Si el usuario **ya nombró piezas concretas** → instala **solo esas**; confirma en una línea la lista y **no** muestres el menú numerado.
4. En cualquier otro caso, **pregunta una sola vez**, sin catálogo detallado:
   - ¿Quieres **todo** el setup-roy, o **solo piezas concretas**?
   - Añade **una línea** de contexto: el pack son skills, agentes y (si existen) workflows bajo `docs/setup-roy/`; en esta versión hay *N* skills y *M* agentes (y workflows/orchestrator solo si aplican). **No** listes cada pieza ni objetivos en este turno.
5. Si responde **todo** → copia el árbol completo de `setup-roy/`. No hace falta volcar el catálogo antes de copiar.
6. Si responde **a medida** / piezas concretas → muestra **una sola vez** la **lista numerada** de piezas instalables (no repitas el mismo menú en turnos posteriores salvo que el usuario lo pida). En cada ítem: **nombre** (id estable, p. ej. `companion`, `coder`) y **objetivo en una o dos frases**.
   - **Orden del menú** (los números dependen de este orden en la sesión):
     1. Skills: carpetas bajo `skills/` con `SKILL.md`, ordenadas por **id de carpeta A→Z**.
     2. Agentes: archivos `agents/*.md` (excluye `agents.md` raíz del pack), ordenados por **nombre de archivo A→Z**.
     3. Workflows: archivos en `workflows/`, A→Z por nombre de archivo.
     4. `orchestrator/` como ítem aparte solo si existe.
   - Indica al usuario que puede responder con **ids** o **nombres** (p. ej. `sdd, ftd, coder`) o con **números** de ese menú (p. ej. `7, 4, 11` si en esta sesión sdd es el 7, ftd el 4 y coder el 11).
   - Texto del objetivo: léelo del pack; resume en el idioma del usuario si hace falta, sin inventar. Orden de preferencia:
     - Skills: campo `description` del frontmatter de `skills/<id>/SKILL.md`.
     - Agentes: primera frase útil bajo `## Role` o `## When to use` en `agents/<id>.md`.
     - Workflows / orchestrator: título o primer párrafo del `.md`.
   - No dupliques rutas anidadas basura (p. ej. no listes `skills/skills/...` como ítem aparte).
7. Tras la elección en modo a medida → copia **solo** las rutas elegidas más `agents.md` en la raíz del pack.
8. Antes de cerrar, confirma qué quedó instalado (lista corta con rutas).

Si `docs/setup-roy/` **ya existe**, pregunta antes de tocar: ¿añadir piezas, reinstalar todo (sustituir árbol), o cancelar?

### Reglas duras

- Destino del pack: `docs/setup-roy/` en la raíz del proyecto actual.
- Origen: **solo** el directorio `setup-roy/` del repositorio setup-ia.
- **No** copies al proyecto `README.md`, `INSTALL.md` ni nada fuera de `setup-roy/`.
- No inventes rutas distintas (`setup/`, `.cursor/`, etc.) salvo que el usuario lo pida explícitamente.
- No hagas commit ni push como parte de la instalación salvo pedido explícito.
- Modo **añadir piezas**: no borres lo ya instalado; solo copia las rutas nuevas que falten.
- Modo **reinstalar todo**: sustituye el árbol entero por la copia nueva.

### Procedimiento

Desde la **raíz del proyecto destino**. URL canónica: `https://github.com/roypm/setup-ia` (salvo que el usuario indique otra).

1. **Obtener el pack** (elige una vía; borra temporales al terminar):
   - **Con git:** `git clone --depth 1 <url> /tmp/setup-ia` y usa `/tmp/setup-ia/setup-roy/`.
   - **Sin git:** descarga el ZIP de `main`, extrae y usa la carpeta `setup-ia-main/setup-roy/` (o el nombre que traiga el archive).
2. **Copiar** según la elección del usuario:
   - **Todo:** crea `docs/` si no existe; copia el contenido de `setup-roy/` → `docs/setup-roy/`.
   - **A medida:** crea `docs/setup-roy/` y `agents.md`; copia solo las carpetas/archivos elegidos manteniendo la misma estructura relativa (p. ej. `skills/companion/`, `agents/coder.md`, `workflows/git-flow.md`).
3. **Cablear:** en `AGENTS.md` de la raíz, asegura el [snippet canónico](#snippet-canonico) una sola vez.
4. **Verificar** con el checklist de abajo.

### Verificación (obligatoria)

- [ ] Existe `docs/setup-roy/agents.md`
- [ ] Cada pieza elegida está en su ruta bajo `docs/setup-roy/`
- [ ] `AGENTS.md` en la raíz contiene el marcador `## Setup Roy` exactamente una vez
- [ ] No se copiaron al proyecto `README.md` ni `INSTALL.md` del meta-repo

### Respuesta al usuario

Resume en pocas líneas: todo vs a medida, piezas instaladas, rutas tocadas, checklist de [verificación](#verificación-obligatoria), y que el contexto del pack está en `docs/setup-roy/agents.md`.

Si acabas de **crear** `AGENTS.md` o de **añadir** el marcador `## Setup Roy`, incluye el [snippet canónico](#snippet-canonico) literal en la respuesta para que el usuario pueda comprobarlo.

---

## Atajo humano (sin IA)

1. Descarga o clona https://github.com/roypm/setup-ia y localiza la carpeta `setup-roy/`.
2. Crea `docs/` en tu proyecto si no existe.
3. Copia todo `setup-roy/` → `docs/setup-roy/`, o solo las carpetas/archivos que quieras (misma estructura).
4. En la raíz, crea o edita `AGENTS.md` y pega el [snippet canónico](#snippet-canonico) si falta el marcador `## Setup Roy`.
5. Comprueba que existe `docs/setup-roy/agents.md`.

---

## Después de instalar

Contexto del pack en `docs/setup-roy/agents.md`; el detalle vive en los archivos bajo ese árbol. No hace falta releer este `INSTALL.md` para usar el pack.
