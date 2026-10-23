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

1. **Obtén el pack** primero (clone o ZIP; ver [Procedimiento](#procedimiento)) para saber qué hay en la versión actual.
2. Si el usuario **ya dijo** “todo”, “completo”, “el pack entero” → instala **todo** `setup-roy/` sin más preguntas.
3. Si el usuario **ya nombró piezas concretas** (p. ej. “solo companion y grilling”) → instala **solo esas**; confirma en una línea la lista y no hagas el menú completo.
4. En cualquier otro caso, **pregunta una vez**:
   - ¿Quieres **todo** el setup-roy, o **solo piezas concretas**?
   - Si preguntas por “todo”, resume en la misma pregunta **nombres** de lo que incluye (una línea por pieza: nombre + para qué sirve). No hace falta un ensayo; basta que el usuario entienda el alcance.
5. Si responde **todo** → copia el árbol completo de `setup-roy/`.
6. Si responde **a medida** / piezas concretas → muestra una **lista numerada** de piezas instalables. En cada ítem: **nombre** (id estable, p. ej. `companion`, `coder`, `git-flow`) y **objetivo en una o dos frases** — qué problema resuelve o cuándo usarla.
   - Texto del objetivo: léelo del pack, no lo inventes. Orden de preferencia:
     - Skills: campo `description` del frontmatter de `skills/<id>/SKILL.md`.
     - Agentes: primera frase útil bajo `## Role` o `## When to use` en `agents/<id>.md`.
     - Workflows / orchestrator: título o primer párrafo del `.md`.
   - Piezas a listar: cada carpeta directa bajo `skills/` que tenga `SKILL.md`; cada `agents/*.md` (no confundir con `agents.md` raíz); cada archivo en `workflows/`; `orchestrator/` si existe. No dupliques rutas anidadas basura (p. ej. no listes `skills/skills/...` como ítem aparte).
7. El usuario elige por **números**, **ids** o **nombres** (p. ej. `1,3,5` o `companion, grilling`). Copia **solo** esas rutas más `agents.md` en la raíz del pack.
8. Antes de cerrar, confirma qué quedó instalado (lista corta).

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

Resume en pocas líneas: todo vs a medida, piezas instaladas, rutas tocadas, si el marcador era nuevo, y que el contexto del pack está en `docs/setup-roy/agents.md`.

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
