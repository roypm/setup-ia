# Instalar y actualizar setup-roy

Este archivo define el contrato de instalación por IA. El objetivo es llevar recursos reutilizables para trabajar con IA a cualquier proyecto y mantenerlos actualizados. El contenido se descubre en cada ejecución: añadir, quitar o reorganizar recursos del pack no exige modificar este contrato.

## Qué verás en el chat

Si pides instalar sin indicar alcance, la IA pregunta una vez si quieres **todo** o **solo piezas**. Si eliges piezas, muestra un menú construido a partir del contenido disponible, con nombre, ruta y propósito. Puedes responder con nombres, rutas o números de ese menú. Si ya indicaste el alcance, no repite la pregunta.

Al terminar muestra las rutas instaladas y el resultado de la verificación. Si ya existe una instalación, aplica las reglas de mantenimiento.

## Qué verás al actualizar

La IA compara la instalación con el origen y muestra lo nuevo, lo distinto y lo que ya no publica el pack, dentro del alcance instalado. Después pregunta una vez por el modo, salvo que ya lo hayas indicado:

- **Integrar:** añade y sobrescribe desde el origen, conservando archivos que solo existen localmente. Advierte que las ediciones locales de archivos sobrescritos se pierden.
- **Reinstalar:** restaura los archivos del pack dentro del alcance; puede eliminar archivos gestionados que ya no publica el origen. Informa de los borrados antes de ejecutarlos.
- **Solo añadir:** copia únicamente rutas ausentes, conservando el contenido existente.
- **Cancelar:** termina sin modificar la instalación.

Puedes evitar preguntas indicando «Instala todo setup-roy», «Actualiza setup-roy integrando» o «Solo añade lo nuevo». Una actualización parcial conserva la selección anterior; una instalación completa incorpora también los nuevos recursos del pack.

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
- Si no indicó alcance, pregunta una vez «¿Todo setup-roy o solo piezas concretas?» con una frase sobre su objetivo, sin catálogo previo.
- Copia la selección y sus dependencias manteniendo la estructura relativa. No traslades plantillas ni archivos internos a otras partes del proyecto por el mero hecho de instalarlos.
- Si el destino ya contiene archivos, entra en mantenimiento. Una petición explícita de añadir piezas copia solo rutas ausentes y amplía la selección registrada; no sobrescribe ni borra lo existente.
- Crea o actualiza el registro de instalación y el enlace de `AGENTS.md` tras completar las operaciones.

### Registro de instalación

Mantén `docs/setup-roy/.setup-roy-install.json` como metadato local generado por el instalador. Esta ruta está reservada: si el origen la publica o ya existe con contenido ajeno al registro, informa del conflicto antes de modificarla. No la trates como contenido del pack ni como huérfano.

Usa JSON con estos campos:

- `schema_version`: `1`.
- `source`: objeto con `location` y `ref` utilizados, y `revision` exacta o `null` si no se conoce.
- `selection`: objeto con `mode` (`all` o `partial`) y `paths` (rutas relativas de las unidades elegidas; vacío en modo `all`).
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
6. Para instalaciones anteriores sin registro, o con registro ilegible o de versión desconocida, no deduzcas propiedad ni selección a partir de la mera presencia de archivos. Muestra el inventario y pregunta por el alcance y el modo en una sola consulta si ambos faltan. Si el usuario ya los especificó, procede. Conserva los archivos de propiedad desconocida; registra solo lo que copies. No reemplaces un registro desconocido sin aclarar su recuperación.

#### Informe de sincronización con el pack upstream

Genera el informe antes de copiar, incluso con modo explícito. Indica origen, referencia, revisión disponible y alcance:

| Estado | Significado dentro del alcance |
|--------|--------------------------------|
| Nuevo | Existe en el origen y falta localmente. |
| Diferente | Existe en ambos con distinto contenido. Señala las ediciones locales detectadas respecto al hash registrado. |
| Al día | Existe en ambos con el mismo contenido. |
| Retirado del origen | Estaba gestionado y ya no pertenece al contenido vigente del alcance. |
| Solo local, sin propiedad conocida | No lo publica el origen y no consta como gestionado. |

No presentes las piezas fuera del alcance como faltantes. Excluye el registro del diff del pack. Resume conteos y rutas relevantes; informa de las colisiones con archivos locales que la copia sobrescribiría.

#### Aplicación del modo

Si el usuario ya indicó modo (integrando/sincronizar/merge, reinstalar/copia limpia, o solo añadir/no sobrescribir), aplícalo sin repetir la pregunta. En otro caso ofrece una vez los modos descritos al inicio.

- **Integrar:** copia rutas nuevas y diferentes dentro del alcance. Conserva retirados y archivos solo locales, e informa de los que permanecen. Avisa de las sobrescrituras antes de ejecutarlas.
- **Solo añadir:** copia rutas ausentes dentro del alcance. No sobrescribas, borres ni marques como copiados los archivos que ya existían.
- **Reinstalar:** copia el contenido vigente dentro del alcance y elimina únicamente los archivos retirados cuya propiedad esté registrada. Lista antes los borrados previstos. Conserva los archivos locales sin propiedad conocida y los archivos fuera del alcance. Si el usuario pide borrar también archivos propios, concreta esas rutas y requiere autorización explícita para ese borrado. No borres el directorio completo como atajo.
- **Cancelar:** no copies, borres ni actualices el registro o `AGENTS.md`.

Una dependencia que deje de necesitarse se trata como retirada solo si ninguna selección conservada la requiere. Si en una operación limitada otra pieza instalada todavía necesita el archivo, consérvalo. Los bloqueos de tipo archivo/carpeta o enlaces deben resolverse antes de sobrescribir; no borres contenido desconocido para forzar una copia.

### Snippet canónico

En `AGENTS.md` de la raíz, asegura una sola sección con el marcador `## Setup Roy`:

```markdown
## Setup Roy
Optional resources for AI-assisted work are installed in `docs/setup-roy/`. When the user names a resource or the task clearly fits the pack, inspect the installed tree and its available guidance, then read the relevant resources and follow those that apply. Use only paths that actually exist. Otherwise work normally.
```

Si existe la sección de una instalación anterior, actualiza solo ese bloque hasta el siguiente encabezado del mismo nivel o superior; conserva las demás instrucciones del proyecto. Si tiene personalizaciones, conserva las compatibles y explica cualquier conflicto antes de reemplazarlas. Si hay marcadores duplicados, unifícalos conservando el contenido propio. No obligues a abrir un archivo interno cuyo nombre pueda cambiar o que no esté instalado.

### Verificación obligatoria

- Las rutas elegidas y sus dependencias necesarias existen bajo el destino; no se copiaron piezas fuera del alcance.
- Los archivos copiados coinciden con la instantánea de origen y conservan sus rutas relativas.
- El registro es JSON válido y refleja la selección, procedencia y archivos realmente gestionados.
- `AGENTS.md` contiene el marcador una sola vez y conserva las instrucciones ajenas al pack.
- No se copiaron archivos de fuera del directorio distribuible.
- Integrar y solo añadir conservaron los archivos locales y retirados; reinstalar eliminó únicamente los archivos autorizados dentro del alcance.
- Se han comunicado sobrescrituras, retiradas, dependencias no resueltas y cambios parciales si los hubo.

### Respuesta al usuario

Resume el modo, alcance, rutas tocadas, archivos locales o retirados conservados y resultado de la verificación. Si creaste o modificaste el bloque de `AGENTS.md`, muestra el texto final. No declares completa una instalación con dependencias necesarias sin resolver.

## Instalación manual

Puedes obtener una instantánea del origen y copiar todo o una selección con sus dependencias a `docs/setup-roy/`, conservando sus rutas relativas, y añadir el snippet a `AGENTS.md`. Usa las mismas reglas de alcance y conservación al actualizar. Para mantener historial de propiedad, crea el registro descrito arriba; sin él, la siguiente actualización tratará los archivos existentes como una instalación anterior sin registro.

## Después de instalar

La IA descubre los recursos disponibles en el árbol instalado según su objetivo y las instrucciones del proyecto. No hace falta releer este contrato para usar el pack; sí para instalarlo o mantenerlo.
