# Instalar setup-roy

Instalación **solo por IA**: este archivo es el contrato. No hay script en el meta-repo; la IA obtiene el pack y lo deja en el proyecto destino.

## Qué verás en el chat

Para ti (la IA sigue las reglas de [Contrato para la IA](#contrato-para-la-ia) más abajo):

1. **Primer turno:** si no dijiste ya “todo” o nombres concretos de piezas, te preguntará una vez si quieres **todo** setup-roy o **solo piezas**.
2. **Todo:** copia el pack completo a `docs/setup-roy/` y cablea `AGENTS.md`; suele bastar un resumen corto (cuántos skills, workflows, etc. hay en esta versión).
3. **A medida:** te muestra **una vez** un menú numerado (nombre + para qué sirve cada pieza). Respondes con **ids** o nombres (`sdd, companion`), o con **números** del menú (`2, 5, 9`).
4. **Primera instalación** con `docs/setup-roy/` ya presente: pregunta antes de tocar (ver [mantenimiento](#mantenimiento-y-actualización)).
5. **Al terminar:** lista breve de lo instalado y comprobación de rutas; si creó o tocó `AGENTS.md`, verás el [snippet canónico](#snippet-canonico).

Puedes acortar el diálogo diciendo en el primer mensaje, por ejemplo: «Instala todo setup-roy» o «Solo sdd, ftd y companion».

## Qué verás al actualizar

Cuando pidas **actualizar**, **sincronizar** o **integrar** setup-roy (o la IA detecte que ya está instalado y el pedido es de mantenimiento):

1. **Informe de sincronización** respecto al pack en setup-ia (`main` salvo otra URL): conteos y listas cortas por [categoría](#informe-de-sincronización-con-el-pack-upstream).
2. **Una pregunta** (salvo atajo): **integrar**, **reinstalar**, **solo añadir** lo que falta, o **cancelar**.
3. **Integrar** (recomendado): trae lo nuevo del pack y sobrescribe archivos que el pack sigue publicando; **no borra** carpetas ni ficheros que solo existen en tu repo ([huérfanos](#informe-de-sincronización-con-el-pack-upstream)).
4. **Reinstalar:** sustituye el árbol (o el alcance acordado) como copia limpia del pack; **elimina** huérfanos. Aviso explícito antes de ejecutar.
5. **Solo añadir:** copia rutas que aún no existen localmente; no sobrescribe lo ya presente.
6. **Al terminar:** qué se tocó, huérfanos que siguen en disco (si integrar o solo añadir), checklist de [verificación](#verificación-obligatoria).

Atajos en el primer mensaje: «Actualiza setup-roy **integrando**», «**Reinstala** setup-roy», «Solo **añade** lo nuevo del pack».

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
| **Atajo con piezas** | En el primer mensaje ya nombra ids o nombres (`solo sdd, ftd y companion`) |
| **Integrar** / actualizar sin borrar | `integrando`, `sync`, `sincronizar`, `actualizar sin borrar`, `merge del pack` |
| **Reinstalar** | `sustituir todo`, `copia limpia`, `reinstalar setup-roy` |
| **Solo añadir** (mantenimiento) | `solo lo nuevo`, `añadir piezas nuevas`, `no sobrescribir` |

1. **Obtén el pack** primero (clone o ZIP; ver [Procedimiento](#procedimiento)) para saber qué hay en la versión actual.
2. Si el usuario **ya pidió todo** (tabla anterior) → instala **todo** `setup-roy/` sin menú; opcional: una línea con el recuento (N skills, M agentes, workflows si hay).
3. Si el usuario **ya nombró piezas concretas** → instala **solo esas**; confirma en una línea la lista y **no** muestres el menú numerado.
4. En cualquier otro caso, **pregunta una sola vez**, sin catálogo detallado:
   - ¿Quieres **todo** el setup-roy, o **solo piezas concretas**?
   - Añade **una línea** de contexto: el pack son skills, agentes y (si existen) workflows bajo `docs/setup-roy/`; en esta versión hay *N* skills y *M* agentes (y workflows/orchestrator solo si aplican). **No** listes cada pieza ni objetivos en este turno.
5. Si responde **todo** → copia el árbol completo de `setup-roy/`. No hace falta volcar el catálogo antes de copiar.
6. Si responde **a medida** / piezas concretas → muestra **una sola vez** la **lista numerada** de piezas instalables (no repitas el mismo menú en turnos posteriores salvo que el usuario lo pida). En cada ítem: **nombre** (id estable, p. ej. `companion`, `sdd`) y **objetivo en una o dos frases**.
   - **Orden del menú** (los números dependen de este orden en la sesión):
     1. Skills: carpetas bajo `skills/` con `SKILL.md`, ordenadas por **id de carpeta A→Z**.
     2. Agentes: carpetas `agents/<id>/` que contienen `agent.md`, ordenadas por **id A→Z** (excluye `agents.md` raíz del pack).
     3. Workflows: archivos en `workflows/`, A→Z por nombre de archivo.
     4. `orchestrator/` como ítem aparte solo si existe.
   - Indica al usuario que puede responder con **ids** o **nombres** (p. ej. `sdd, ftd, companion`) o con **números** de ese menú (p. ej. `7, 4, 11` si en esta sesión sdd es el 7, ftd el 4 y companion el 11).
   - Texto del objetivo: léelo del pack; resume en el idioma del usuario si hace falta, sin inventar. Orden de preferencia:
     - Skills: campo `description` del frontmatter de `skills/<id>/SKILL.md`.
     - Agentes: primera frase útil bajo `## Role` o `## When to use` en `agents/<id>/agent.md`.
     - Workflows / orchestrator: título o primer párrafo del `.md`.
   - No dupliques rutas anidadas basura (p. ej. no listes `skills/skills/...` como ítem aparte).
7. Tras la elección en modo a medida → copia **solo** las rutas elegidas más `agents.md` en la raíz del pack.
8. Antes de cerrar, confirma qué quedó instalado (lista corta con rutas).

Si `docs/setup-roy/` **ya existe** y el usuario **no** pidió explícitamente una primera instalación en vacío, entra en [Mantenimiento y actualización](#mantenimiento-y-actualización) (no asumas “instalar encima” sin modo).

### Mantenimiento y actualización

Activa cuando el usuario pida **actualizar**, **sincronizar**, **integrar** o **reinstalar** setup-roy, o cuando vaya a tocar un `docs/setup-roy/` ya existente salvo instalación nueva acordada.

**Referencia:** el pack **upstream** es el directorio `setup-roy/` del repo setup-ia (URL canónica en [Procedimiento](#procedimiento)). La comparación es **local `docs/setup-roy/` vs ese upstream**, no el git remoto del proyecto destino.

#### Informe de sincronización con el pack upstream

Genera el informe **antes** de copiar (salvo que el usuario canceló tras verlo). Usa estas etiquetas en el idioma del usuario:

| Etiqueta | Significado |
|----------|-------------|
| **Nuevo en el pack** | Ruta presente en upstream, ausente en local. |
| **Actualizable** | Misma ruta relativa en ambos; contenido distinto (p. ej. diff o checksum). En **integrar**, upstream gana: se sobrescribe. |
| **Al día** | Misma ruta; contenido equivalente. En **integrar**, no hace falta copiar. |
| **Huérfano del pack** | Existe en local bajo `docs/setup-roy/` pero ya no existe en upstream (o nunca estuvo en el árbol upstream actual). En **integrar** y **solo añadir**, **no borrar**. Listar al cerrar. |

Compara archivos bajo las mismas rutas relativas (p. ej. `skills/sdd/SKILL.md`, `agents.md`, `workflows/01-….md`). No incluyas en el informe archivos fuera de `docs/setup-roy/`.

Resumen breve: conteos por etiqueta; listas acotadas (p. ej. rutas huérfanas y actualizables más importantes). Menciona contra qué revisaste (p. ej. `main` de setup-ia, fecha de la sesión).

#### Elección de modo (una pregunta salvo atajo)

Si el usuario **ya nombró el modo** (tabla de interpretación) → aplícalo; confirma en una línea y **no** repitas el menú.

Si no, tras el informe pregunta **una vez**:

- **Integrar** — actualizar desde upstream sin eliminar huérfanos.
- **Reinstalar** — sustituir por copia limpia del pack (alcance abajo); **borra** huérfanos en ese alcance.
- **Solo añadir** — solo rutas **Nuevo en el pack**; no sobrescribir **Actualizable**.
- **Cancelar**.

**Alcance** (si el usuario no lo dijo):

- Por defecto, **todo** lo instalado bajo `docs/setup-roy/` frente al árbol upstream completo (piezas que existan en upstream se sincronizan; huérfanos se reportan).
- Si pide **piezas concretas**, limita informe y copia a esas piezas más `agents.md` si aplica.

#### Reglas por modo

- **Integrar:** copia desde upstream cada ruta **Nuevo en el pack** y cada **Actualizable** dentro del alcance. Sobrescribe archivos existentes. **No** elimines **Huérfano del pack**. Dentro de una carpeta (p. ej. un skill), un fichero extra solo local se trata como huérfano, no lo borres. Asegura el [snippet canónico](#snippet-canonico) en `AGENTS.md` si falta (no dupliques). Avisa que ediciones locales en rutas **Actualizable** se pierden al integrar.
- **Reinstalar:** avisa que se eliminará lo que no esté en la copia nueva. Sustituye el árbol del alcance (típicamente borrar `docs/setup-roy/` y copiar de nuevo, o equivalente). Luego cablea `AGENTS.md`. Equivalente al modo **reinstalar todo** ya definido para instalación.
- **Solo añadir:** copia solo rutas **Nuevo en el pack**; no modifiques **Actualizable** ni **Al día**. No borres huérfanos. Distinto de “añadir piezas” del menú de instalación a medida (misma mecánica: rutas ausentes).

Tras cualquier modo, confirma rutas tocadas, huérfanos que permanecen (integrar / solo añadir) y el checklist.

### Reglas duras

- Destino del pack: `docs/setup-roy/` en la raíz del proyecto actual.
- Origen: **solo** el directorio `setup-roy/` del repositorio setup-ia.
- **No** copies al proyecto `README.md`, `INSTALL.md` ni nada fuera de `setup-roy/`.
- No inventes rutas distintas (`setup/`, `.cursor/`, etc.) salvo que el usuario lo pida explícitamente.
- No hagas commit ni push como parte de la instalación salvo pedido explícito.
- Modo **añadir piezas** (instalación o mantenimiento): no borres lo ya instalado; solo copia rutas que falten localmente.
- Modo **reinstalar** / **reinstalar todo**: sustituye el árbol del alcance por la copia upstream; elimina huérfanos en ese alcance.
- Modo **integrar**: sobrescribe según upstream; **nunca** borres huérfanos del pack.

### Procedimiento

Desde la **raíz del proyecto destino**. URL canónica: `https://github.com/roypm/setup-ia` (salvo que el usuario indique otra).

1. **Obtener el pack** (elige una vía; borra temporales al terminar):
   - **Con git:** `git clone --depth 1 <url> /tmp/setup-ia` y usa `/tmp/setup-ia/setup-roy/`.
   - **Sin git:** descarga el ZIP de `main`, extrae y usa la carpeta `setup-ia-main/setup-roy/` (o el nombre que traiga el archive).
2. **Copiar** según instalación o [modo de mantenimiento](#reglas-por-modo):
   - **Instalación — todo:** crea `docs/` si no existe; copia el contenido de `setup-roy/` → `docs/setup-roy/`.
   - **Instalación — a medida:** crea `docs/setup-roy/` y `agents.md`; copia solo las carpetas/archivos elegidos manteniendo la misma estructura relativa (p. ej. `skills/companion/`, `skills/sdd/`, `workflows/git-flow.md`).
   - **Integrar / solo añadir / reinstalar:** misma obtención del pack; aplica las reglas del modo (informe previo salvo reinstalar con confirmación explícita ya dada).
3. **Cablear:** en `AGENTS.md` de la raíz, asegura el [snippet canónico](#snippet-canonico) una sola vez.
4. **Verificar** con el checklist de abajo.

### Verificación (obligatoria)

- [ ] Existe `docs/setup-roy/agents.md`
- [ ] Cada pieza elegida está en su ruta bajo `docs/setup-roy/`
- [ ] `AGENTS.md` en la raíz contiene el marcador `## Setup Roy` exactamente una vez
- [ ] No se copiaron al proyecto `README.md` ni `INSTALL.md` del meta-repo
- [ ] Tras **integrar** o **solo añadir**: huérfanos del pack reportados (si los hay), sin borrarlos salvo **reinstalar**

### Respuesta al usuario

Resume en pocas líneas: instalación vs mantenimiento, modo (integrar / reinstalar / solo añadir / todo vs a medida), piezas o rutas tocadas, huérfanos que siguen en disco si aplica, checklist de [verificación](#verificación-obligatoria), y que el contexto del pack está en `docs/setup-roy/agents.md`.

Si acabas de **crear** `AGENTS.md` o de **añadir** el marcador `## Setup Roy`, incluye el [snippet canónico](#snippet-canonico) literal en la respuesta para que el usuario pueda comprobarlo.

---

## Atajo humano (sin IA)

**Instalar**

1. Descarga o clona https://github.com/roypm/setup-ia y localiza la carpeta `setup-roy/`.
2. Crea `docs/` en tu proyecto si no existe.
3. Copia todo `setup-roy/` → `docs/setup-roy/`, o solo las carpetas/archivos que quieras (misma estructura).
4. En la raíz, crea o edita `AGENTS.md` y pega el [snippet canónico](#snippet-canonico) si falta el marcador `## Setup Roy`.
5. Comprueba que existe `docs/setup-roy/agents.md`.

**Actualizar**

- **Integrar:** copia desde upstream encima de `docs/setup-roy/` (sobrescribe lo que coincida en ruta; no borres en local lo que ya no venga en el pack).
- **Reinstalar:** borra `docs/setup-roy/` y vuelve a copiar el árbol deseado desde `setup-roy/`.
- **Solo añadir:** copia únicamente archivos o carpetas que aún no existan en tu `docs/setup-roy/`.

---

## Después de instalar

Contexto del pack en `docs/setup-roy/agents.md`; el detalle vive en los archivos bajo ese árbol. No hace falta releer este `INSTALL.md` para usar el pack.
