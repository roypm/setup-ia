# Instalar y actualizar setup-roy

Este archivo define el contrato de instalación por IA. El objetivo es llevar recursos reutilizables para trabajar con IA a cualquier proyecto y mantenerlos actualizados. El contenido se descubre en cada ejecución: añadir, quitar o reorganizar recursos del pack no exige modificar este contrato.

## Qué verás en el chat

Si pides instalar sin indicar alcance, la IA se detiene y pregunta una vez si quieres **todo** o **solo piezas**. No copia nada hasta que respondas. Si eliges piezas, muestra un menú construido a partir del contenido disponible, con nombre, ruta y propósito. Puedes responder con nombres, rutas o números de ese menú. Si ya indicaste el alcance, no repite la pregunta. Enlazar este archivo, o decir «según INSTALL.md», activa el contrato; no equivale a pedir el pack completo.

Al terminar muestra las rutas instaladas y el resultado de la verificación. Si ya existe una instalación, aplica las reglas de mantenimiento.

## Qué verás al actualizar

La IA lee el registro (si existe), toma una instantánea del origen y muestra un **informe en dos bloques** (sin copiar hasta que elijas, salvo que ya hayas indicado el plan completo en el mismo mensaje):

**Peticiones genéricas.** Frases como «Actualiza setup-roy en este proyecto según …/INSTALL.md» (con enlace o referencia a este archivo) **activan el contrato** pero **no nombran un plan** de mantenimiento. Equivalen a pedir el informe y el menú: **no autorizan copiar** en ese turno. Hasta que respondas (o mandes un atajo inequívoco en un mensaje nuevo), la IA no modifica archivos bajo `docs/setup-roy/`, no crea ni reescribe `.setup-roy-install.json` y no toca el bloque `## Setup Roy` en `AGENTS.md`. No trates «actualizar» o «según INSTALL.md» como sinónimo de integrar alcance, tomar origen ni añadir catálogo.

**A — Dentro de tu alcance registrado** (lo que promete `selection` y dependencias): al día, actualizable, hueco en disco, retirado del pack, solo local.

**B — En el pack upstream, no en tu proyecto:** piezas **sin instalar** (están en remoto, no en disco y no constan en tu selección) y, aparte, **nuevo en el pack para este proyecto** (unidad que el origen publica ahora y que no figura en `managed_files` ni en `selection.paths` / `dependencies`; se clasifica con el registro y el árbol, sin comparar historial de revisiones del meta-repositorio).

Tras el informe, **dos pasos** salvo que lo resuelvas en una sola frase:

1. **Qué conjuntos tocar:** reparar huecos, actualizar lo distinto del bloque A, añadir del catálogo (bloque B: sin instalar y/o nuevo en el pack), alinear en disco todo el pack upstream (opcional, sin cambiar `mode` a `all` por defecto), reinstalar solo el alcance registrado, o cancelar.
2. **Solo si vas a tocar lo actualizable:** conservar tus archivos locales o tomar el contenido del origen (sobrescribir; aviso de pérdida de ediciones). Variante fuerte: sobrescribir **todo** lo gestionado desde el origen aunque la selección siga en `partial`.

**Atajos en un solo mensaje** (sí autorizan copiar en ese turno si el plan queda claro; muestra el informe y aplica sin repetir el menú):

- **Integrar alcance** / «Actualiza setup-roy integrando» — huecos + nuevos archivos dentro del alcance + actualizables **tomando origen**; no añade unidades del catálogo (bloque B).
- **Solo añadir en mi alcance** — ausentes **solo** dentro del alcance; sin sobrescribir; **no** incluye piezas del catálogo que nunca instalaste.
- **Añadir del catálogo** / **añade del pack lo que no tengo** — copia unidades del bloque B que indiques (o un menú), sin sobrescribir lo existente; amplía `selection.paths`.
- **Mix** — combina lo que pidas (p. ej. actualizar instalado + añadir del catálogo); en un mensaje puedes decir «mix: integra lo distinto y añade ponyskill X».
- **Sincronizar pack en disco** — copia todo lo que falte del upstream y, si lo pides, alinea lo gestionado; no pasa a `mode: all` salvo petición explícita de mantener el pack entero a futuro.
- **Reinstalar alcance** — copia limpia dentro del alcance registrado; puede borrar gestionados retirados del origen (con lista previa).
- **Cancelar** — sin cambios.

Frases ambiguas como «solo añade lo nuevo» obligan a **aclarar una vez**: ¿solo huecos y archivos nuevos **dentro** del alcance, o también piezas del remoto que no tienes instaladas?

`selection.mode: partial` conserva tu contrato de mantenimiento aunque el árbol local coincida con todo el pack; `all` significa que en futuras actualizaciones el alcance es el pack completo.

## Contrato para la IA

Activa este contrato cuando el usuario pida instalar, configurar, ampliar o mantener setup-roy en un proyecto. Habla en su idioma y conserva el idioma original de los recursos. Los nombres y categorías del contenido no forman parte del contrato.

### Origen y destino

- Origen canónico: `https://github.com/roypm/setup-ia`, referencia `main`, salvo indicación del usuario. El contenido distribuible es exclusivamente su directorio `setup-roy/`.
- Destino: `docs/setup-roy/` en la raíz del proyecto, salvo petición explícita de otro destino; adapta entonces las rutas del enlace en `AGENTS.md` y del registro.
- Obtén una instantánea del origen mediante Git o archivo descargado. Usa un temporal único y elimina solo los temporales creados por esta ejecución. Respeta la referencia solicitada y registra su revisión exacta cuando esté disponible.
- Si el usuario proporciona una copia local, úsala e identifica su procedencia. Si no puedes obtener el origen, explica el bloqueo; no presentes una copia local como actualización remota verificada.
- No copies archivos del meta-repositorio situados fuera de `setup-roy/`. Un archivo con el mismo nombre situado dentro del pack sí puede ser un recurso válido.
- No hagas commit ni push salvo petición explícita.

### Descubrimiento por propósito

1. Explora recursivamente la instantánea real del pack. Lee sus instrucciones de orientación si existen; ningún archivo interno es obligatorio por su nombre.
2. Identifica unidades que puedan instalarse y usarse con sentido propio a partir de su documentación y estructura. Una unidad puede ser un archivo o una carpeta con sus recursos auxiliares. No presupongas categorías, profundidad, extensiones ni nombres de entrada.
3. Para una selección parcial, construye el menú dinámicamente, ordenado por ruta relativa. Muestra nombre, ruta única y propósito obtenido de la descripción, título o contenido. No inventes objetivos; señala las piezas cuyo propósito no se pueda determinar. Evita listar por separado los auxiliares de una unidad.
4. Acepta nombres inequívocos, rutas o números del menú de esta sesión. Si un nombre resulta ambiguo o no existe, acláralo antes de copiar esa selección.
5. Lee las piezas elegidas y resuelve los recursos internos que necesitan para funcionar, de forma transitiva y sin duplicados. Distingue las dependencias necesarias de los ejemplos, enlaces informativos y alternativas opcionales. Conserva sus rutas relativas y auxiliares. Si necesitas ampliar la selección para que funcione, explica qué dependencias se incluyen y por qué; pide aclaración solo si requiere elegir una alternativa o contradice una exclusión del usuario. No inventes archivos ausentes: informa del bloqueo de la pieza afectada.
6. Los recursos de orientación general solo se incluyen si existen y son necesarios para usar la selección. No incluyas todo el pack por una referencia genérica a explorar su contenido.

El menú y el resumen se generan con lo descubierto. No mantengas un catálogo duplicado ni recuentos fijos en este contrato, el README o las instrucciones de entrada.

### Primera instalación y ampliación

- Si el usuario pidió **todo** (también completo, entero, full o all), copia todo el contenido distribuible sin menú.
- Si nombró piezas, resuelve directamente esa selección; si pidió una selección sin concretar, muestra el menú una vez.
- Si no indicó alcance, no copies, no crees el registro ni toques `AGENTS.md`. Pregunta una vez «¿Todo setup-roy o solo piezas concretas?» con una frase sobre su objetivo, sin catálogo previo, y espera la respuesta.
- `mode: all` solo vale si el usuario pidió el pack entero en esta petición o en la respuesta a esa pregunta. No lo infieras porque el proyecto esté vacío, no tenga `AGENTS.md`, no exista `docs/setup-roy/`, el destino no tenga archivos, el pack «sirva entero» o el usuario haya enlazado este contrato sin decir todo.
- Copia la selección y sus dependencias manteniendo la estructura relativa. No traslades plantillas ni archivos internos a otras partes del proyecto por el mero hecho de instalarlos.
- Si el destino ya contiene archivos, entra en mantenimiento. Una petición explícita de añadir piezas copia solo rutas ausentes y amplía la selección registrada; no sobrescribe ni borra lo existente.
- Crea o actualiza el registro de instalación y el enlace de `AGENTS.md` tras completar las operaciones.

### Registro de instalación

Mantén `docs/setup-roy/.setup-roy-install.json` como metadato local generado por el instalador. Esta ruta está reservada: si el origen la publica o ya existe con contenido ajeno al registro, informa del conflicto antes de modificarla. No la trates como contenido del pack ni como huérfano.

Usa JSON con estos campos:

- `schema_version`: `1`.
- `source`: objeto con `location` y `ref` utilizados, y `revision` exacta o `null` si no se conoce.
- `selection`: objeto con `mode` (`all` o `partial`) y `paths` (rutas relativas de las unidades elegidas; vacío en modo `all`). `partial` describe qué unidades mantienes en el contrato de actualización; no exige que falten archivos del pack en disco. Pasa a `all` solo con petición explícita de mantener el pack entero.
- `dependencies`: rutas relativas de las dependencias resueltas para la selección.
- `managed_files`: objeto que relaciona cada archivo realmente copiado con su SHA-256 después de copiarlo. Conserva las entradas de archivos gestionados que permanecen en disco, incluso si desaparecen del origen. Elimina entradas de archivos ausentes. No te atribuyas archivos preexistentes que no hayas copiado.

Las rutas son relativas al pack, sin rutas absolutas ni segmentos `..`. Distingue archivos de carpetas usando el árbol de origen; una carpeta seleccionada incluye sus descendientes. No sigas enlaces que escapen del pack o del destino. No sobrescribas archivos a través de enlaces locales.

`source` identifica la última instantánea consultada; no implica que todos los archivos se hayan actualizado. Los hashes describen la última copia de cada archivo y permiten detectar ediciones locales. En **solo añadir**, conserva los hashes anteriores de archivos no sobrescritos. Actualiza el registro únicamente con operaciones completadas; si una copia falla, informa de los cambios parciales sin declarar éxito.

### Mantenimiento y actualización

#### Alcance

1. Lee el registro antes de comparar. Conserva por defecto su origen y referencia salvo petición de cambio.
2. Con selección `all`, el alcance es todo el pack de la instantánea actual más los archivos gestionados previamente.
3. Con selección `partial`, conserva las rutas elegidas y resuelve de nuevo sus dependencias. Los nuevos archivos dentro de carpetas seleccionadas entran en alcance; las nuevas piezas fuera de ellas no se añaden automáticamente. Incluye los archivos antes gestionados bajo ese alcance y las dependencias anteriores para informar de retiradas.
4. Si el usuario limita la operación a piezas concretas, modifica solo ese alcance. Conserva en el registro las selecciones y archivos gestionados ajenos a la operación. Añadir piezas amplía una selección parcial; no convierte una selección completa en parcial.
5. Si una ruta seleccionada desaparece o cambia de ubicación, informa de ello. No asumas equivalencias ni conviertas la instalación en completa; conserva la selección pendiente hasta que el usuario elija sustituirla o retirarla.
6. Para instalaciones anteriores sin registro, o con registro ilegible o de versión desconocida, no deduzcas propiedad ni selección a partir de la mera presencia de archivos. Muestra el inventario (y el informe A/B cuando puedas) y pregunta por el alcance y el modo en **una sola consulta** si ambos faltan. **Hasta la respuesta del usuario**, no copies, no crees el registro y no declares un `partial` inferido como contrato vigente. Si el usuario ya nombró alcance y un atajo/plan de la lista permitida, procede. Conserva los archivos de propiedad desconocida; registra solo lo que copies en operaciones autorizadas. No reemplaces un registro desconocido sin aclarar su recuperación.

#### Informe de sincronización con el pack upstream

Genera el informe **antes** de copiar en el mismo turno. Si el mensaje del usuario **no** autoriza un plan (petición genérica de actualización o enlace a este contrato sin atajo), **solo** entrega el informe y el menú de paso 1 (y paso 2 si procede); **termina sin copiar**. No titules el informe «antes de aplicar» ni «plan aplicado» si ya modificaste disco en ese turno sin autorización.

Indica origen, referencia, revisión disponible, `selection.mode` y rutas de alcance cuando el registro exista; sin registro, describe el inventario local sin fijar selección en JSON. Excluye el propio archivo de registro del diff del pack. Resume conteos y rutas; señala colisiones que una sobrescritura tocaría y dependencias rotas (p. ej. workflow instalado que referencia una skill ausente).

Presenta **dos bloques**. No mezcles etiquetas entre bloques ni llames «nuevo» del bloque B a un hueco del bloque A.

**Bloque A — Dentro del alcance registrado**

| Estado | Significado |
|--------|-------------|
| Al día | En disco y coincide con la instantánea upstream (hash o equivalente). |
| Actualizable | En disco y upstream distinto; indica si hay edición local respecto al hash registrado. |
| Hueco en disco | Consta en alcance o `managed_files` pero falta en `docs/setup-roy/`; es reparación, no catálogo. |
| Retirado del origen | Estaba gestionado en el alcance y ya no pertenece al contenido vigente del pack en esa ruta. |
| Solo local, sin propiedad conocida | En disco; no lo publica el origen y no consta como gestionado. |

Archivos nuevos **bajo una carpeta ya en alcance** (p. ej. un archivo extra dentro de `skills/foo/` ya seleccionado) cuentan como hueco o ausente **dentro del alcance**, no como unidad «sin instalar» del bloque B.

**Bloque B — En upstream, no en tu proyecto** (comparación unidad a unidad con el árbol local y el registro)

| Estado | Significado |
|--------|-------------|
| Sin instalar | El origen publica la unidad, no está en disco y **no** consta en `selection.paths` (ni como dependencia resuelta). Incluye piezas que quitaste del proyecto y del registro. |
| Nuevo en el pack (para este proyecto) | Unidad en upstream que **no** consta en `managed_files` ni en `selection.paths` / `dependencies`, y no está en disco. Clasificación por registro y árbol actual; **no** uses diff de historial git del meta-repositorio. Puede coincidir en listados con «sin instalar»; muestra una sola fila por unidad con la etiqueta que aplique (prioriza «nuevo en el pack» si nunca hubo huella en el registro). |

No presentes unidades del bloque B como «faltantes del alcance» del bloque A. Las del bloque A que estén al día no requieren acción salvo que el usuario pida integrar o reinstalar.

#### Plan de actualización (dos pasos)

**Autorización para copiar.** Copiar, sobrescribir, ampliar `selection.paths` o escribir el registro en el primer turno de una actualización requiere que el mensaje del usuario incluya, de forma inequívoca, al menos el **conjunto del paso 1** (p. ej. integrar alcance, añadir del catálogo, mix con partes nombradas). No basta con «actualiza», «mantén», «sincroniza» a secas, «según INSTALL.md» ni el enlace a este archivo. **No** infieras un plan por defecto (p. ej. integrar + tomar origen) aunque el informe muestre pocos actualizables o el bloque B sea grande.

Si el usuario ya describió el plan completo (conjuntos del paso 1 + tratamiento de actualizables cuando hay actualizables en juego), aplícalo sin repetir preguntas. Si la petición es ambigua (p. ej. «añade lo nuevo»), aclara **una vez** y espera.

**Paso 1 — Conjuntos** (ofrece una vez si falta; el usuario puede responder con números, nombres o frases cortas):

| Opción | Efecto |
|--------|--------|
| Reparar huecos | Copia solo rutas del bloque A en estado hueco; no sobrescribe lo existente. |
| Integrar alcance | Huecos del bloque A + archivos nuevos bajo unidades ya en alcance + actualizables del bloque A (paso 2 obligatorio si hay actualizables). |
| Solo añadir en mi alcance | Igual que reparar huecos y ausentes **dentro del alcance**; **no** copia unidades del bloque B; **no** sobrescribe. |
| Añadir del catálogo | Copia unidades elegidas del bloque B (sin instalar / nuevo en el pack); no sobrescribe archivos ya presentes; **amplía** `selection.paths` y dependencias resueltas. Menú una vez si no nombró piezas. |
| Mix | Combina explícitamente las filas anteriores que el usuario indique (p. ej. integrar alcance + añadir del catálogo con lista). |
| Sincronizar pack en disco | Copia todo lo que falte del pack upstream respecto al disco; opcionalmente alinea todo lo gestionado si el usuario lo pide en el mismo mensaje; **no** cambies `selection.mode` a `all` sin petición explícita de mantener el pack entero a futuro. |
| Reinstalar alcance | Copia limpia todo el alcance registrado desde el origen; elimina solo gestionados retirados (lista previa). |
| Cancelar | Sin cambios en disco, registro ni `AGENTS.md`. |

**Paso 2 — Actualizables** (solo si el paso 1 incluye integrar, mix con actualización, sincronizar con alineación, o reinstalar):

- **Conservar local:** no sobrescribas archivos en estado actualizable; informa qué quedó distinto.
- **Tomar origen:** sobrescribe actualizables desde upstream; avisa antes de ejecutar.
- **Sobrescribir todo lo gestionado:** desde upstream, todos los archivos listados en `managed_files` del alcance afectado; compatible con `selection.mode: partial` si el usuario lo pidió; avisa pérdida de ediciones locales.

**Reglas de aplicación**

- **Solo añadir en mi alcance** nunca amplía el catálogo (bloque B) ni sobrescribe.
- **Añadir del catálogo** nunca sobrescribe archivos existentes; siempre amplía selección registrada.
- **Integrar alcance** no añade unidades del bloque B salvo que el paso 1 incluya también añadir del catálogo o mix.
- Cualquier copia de unidades del bloque B actualiza `selection.paths`, `dependencies` y `managed_files` de forma coherente.
- Actualiza `source.revision` solo tras operaciones completadas con éxito.

Una dependencia que deje de necesitarse se trata como retirada solo si ninguna selección conservada la requiere. Si en una operación limitada otra pieza instalada todavía necesita el archivo, consérvalo. Los bloqueos de tipo archivo/carpeta o enlaces deben resolverse antes de sobrescribir; no borres contenido desconocido para forzar una copia.

### Snippet canónico

En `AGENTS.md` de la raíz, asegura una sola sección con el marcador `## Setup Roy`:

```markdown
## Setup Roy
Optional resources for AI-assisted work are installed in `docs/setup-roy/`. When the user names a resource or the task clearly fits the pack, inspect the installed tree and its available guidance, then read the relevant resources and follow those that apply. Use only paths that actually exist. Otherwise work normally.
```

Si existe la sección de una instalación anterior, actualiza solo ese bloque hasta el siguiente encabezado del mismo nivel o superior; conserva las demás instrucciones del proyecto. Si tiene personalizaciones, conserva las compatibles y explica cualquier conflicto antes de reemplazarlas. Si hay marcadores duplicados, unifícalos conservando el contenido propio. No obligues a abrir un archivo interno cuyo nombre pueda cambiar o que no esté instalado.

### Verificación obligatoria

- En actualización, cada copia en el turno estuvo precedida por un plan autorizado en el mensaje del usuario (atajo o plan completo). Una petición genérica con solo enlace a este contrato **no** cumple; la respuesta válida es informe + menú sin cambios en disco.
- Con instalación previa **sin registro**, no se creó ni rellenó `.setup-roy-install.json` ni se fijó `selection` hasta que el usuario respondió al alcance y al modo, salvo que el mismo mensaje ya los nombrara.
- El alcance estaba explícito antes de copiar en instalaciones nuevas. Sin él, la única respuesta válida es la pregunta; una instalación ya hecha en ese caso no es correcta.
- Las rutas elegidas y sus dependencias necesarias existen bajo el destino; no se copiaron piezas fuera del alcance.
- Los archivos copiados coinciden con la instantánea de origen y conservan sus rutas relativas.
- El registro es JSON válido y refleja la selección, procedencia y archivos realmente gestionados.
- `AGENTS.md` contiene el marcador una sola vez y conserva las instrucciones ajenas al pack.
- No se copiaron archivos de fuera del directorio distribuible.
- El informe separó bloque A (alcance) y bloque B (catálogo upstream); «solo añadir en mi alcance» no añadió unidades del bloque B sin petición explícita de catálogo.
- Integrar, solo añadir en alcance y añadir del catálogo respetaron sobrescritura y ampliación de selección según el plan elegido; reinstalar eliminó únicamente los archivos autorizados dentro del alcance.
- `selection.mode` solo pasó a `all` con petición explícita; disco completo con `partial` no se trató como error.
- Se comunicaron sobrescrituras, retiradas, dependencias rotas, dependencias no resueltas y cambios parciales si los hubo.

### Respuesta al usuario

Resume el plan (conjuntos del paso 1 y tratamiento de actualizables), alcance registrado, rutas tocadas, cambios en `selection.paths`, archivos locales o retirados conservados y resultado de la verificación. En actualizaciones, resume ambos bloques del informe aunque no hubiera cambios. Si creaste o modificaste el bloque de `AGENTS.md`, muestra el texto final. No declares completa una instalación con dependencias necesarias sin resolver.

## Instalación manual

Puedes obtener una instantánea del origen y copiar todo o una selección con sus dependencias a `docs/setup-roy/`, conservando sus rutas relativas, y añadir el snippet a `AGENTS.md`. Usa las mismas reglas de alcance y conservación al actualizar. Para mantener historial de propiedad, crea el registro descrito arriba; sin él, la siguiente actualización tratará los archivos existentes como una instalación anterior sin registro.

## Después de instalar

La IA descubre los recursos disponibles en el árbol instalado según su objetivo y las instrucciones del proyecto. No hace falta releer este contrato para usar el pack; sí para instalarlo o mantenerlo.
