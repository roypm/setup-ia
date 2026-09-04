# Instalar setup-roy

Documento de instalación. **La vía principal es la IA**; la sección humana es un atajo opcional.

## Resultado esperado

En la raíz del proyecto destino:

1. Existe `docs/setup-roy/` (pack completo). Se crea `docs/` si no existía.
2. Existe `AGENTS.md` con el [snippet canónico](#snippet-canonico). Se crea el archivo si no existía; si ya tenía el snippet, no se duplica.

---

## Snippet canónico

Marcador: `## Setup Roy`. Texto exacto a añadir en el `AGENTS.md` de la **raíz** del proyecto:

```markdown
## Setup Roy
Si la petición puede cubrirse con el pack en `docs/setup-roy/`, lee primero `docs/setup-roy/agents.md` y sigue su índice. Si no, trabaja con normalidad.
```

---

## Contrato para la IA

Activa este contrato cuando el usuario pida instalar, configurar o añadir **setup-roy** (o este repo) al proyecto actual.

### Reglas duras

- Destino del pack: `docs/setup-roy/` en la raíz del proyecto actual.
- Origen: **solo** el directorio `setup-roy/` de este repositorio.
- **No** copies al proyecto: `README.md`, `INSTALL.md`, `EXTENDING.md`, `bootstrap.py`, ni nada fuera de `setup-roy/`.
- No inventes rutas distintas (`setup/`, `.cursor/`, etc.) salvo que el usuario lo pida explícitamente.
- No hagas commit ni push como parte de la instalación salvo pedido explícito.

### Procedimiento preferido

Desde la raíz del proyecto destino, con la URL del repo `setup-ia` que indique el usuario:

```bash
python bootstrap.py --repo <url-del-repo-setup-ia>
```

El script clona en temporal, copia solo `setup-roy/` → `docs/setup-roy/` y actualiza `AGENTS.md`. Si el pack ya existe y hay que reemplazarlo, usa `--force`. Para simular: `--dry-run`.

Si no puedes ejecutar `bootstrap.py` (no hay red, no hay git, no hay Python, o el script no está disponible), haz el [fallback manual](#fallback-manual).

### Fallback manual

1. Obtén el contenido de `setup-roy/` desde el repo (clone temporal, descarga, o copia local).
2. Crea `docs/` si no existe.
3. Copia `setup-roy/` → `docs/setup-roy/`.
4. Añade el [snippet canónico](#snippet-canonico) a `AGENTS.md` (crear o append; no duplicar si el marcador `## Setup Roy` ya está).
5. Borra temporales de descarga si los creaste.

### Verificación (obligatoria)

Confirma todo esto antes de dar la instalación por hecha:

- [ ] Existe `docs/setup-roy/agents.md`
- [ ] Existen `docs/setup-roy/skills/`, `docs/setup-roy/agents/`, `docs/setup-roy/orchestrator/`, `docs/setup-roy/scripts/`
- [ ] `AGENTS.md` en la raíz contiene el marcador `## Setup Roy` (una sola vez)
- [ ] No se copiaron al proyecto `README.md` / `INSTALL.md` / `EXTENDING.md` / `bootstrap.py` de este repo

Opcional: `python docs/setup-roy/scripts/git_ship.py --dry-run`

### Respuesta al usuario

Resume en pocas líneas: rutas creadas/actualizadas, si el snippet era nuevo o ya estaba, y que el índice de uso es `docs/setup-roy/agents.md`.

---

## Opción humana (manual)

Misma meta que el contrato IA.

1. Copia `setup-roy/` de este repositorio a `docs/setup-roy/` en tu proyecto (crea `docs/` si hace falta).
2. En la raíz, crea o edita `AGENTS.md` y pega el [snippet canónico](#snippet-canonico) (sin duplicarlo).
3. Comprueba que existe `docs/setup-roy/agents.md`.

### Atajo con bootstrap

Si tienes este repo clonado en disco, desde la raíz de tu proyecto:

```bash
python /ruta/a/setup-ia/bootstrap.py --from /ruta/a/setup-ia
```

Opciones: `--dry-run`, `--force` (reescribe el pack si ya existía).

---

## Después de instalar

El índice y la lógica de piezas están en `docs/setup-roy/agents.md`. No hace falta releer este archivo para usar el pack.
