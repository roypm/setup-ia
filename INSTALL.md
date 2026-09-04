# Instalar setup-roy

Documento de instalación. **La vía principal es la IA**; la sección humana es un atajo opcional.

## Resultado esperado

En la raíz del proyecto destino:

1. Existe `docs/setup-roy/` (pack completo). Se crea `docs/` si no existía.
2. Existe `AGENTS.md` con el [snippet canónico](#snippet-canonico). Se crea el archivo si no existía; si ya tenía el snippet, no se duplica.

---

## Snippet canónico

Marcador: `## Setup Roy`. Si ya está en `AGENTS.md`, no lo dupliques. Si no está, añade este bloque en el `AGENTS.md` de la **raíz** del proyecto:

```markdown
## Setup Roy
If the request may be covered by the pack under `docs/setup-roy/`, read `docs/setup-roy/agents.md` first and follow its index. Otherwise work normally.
```

---

## Contrato para la IA

Activa este contrato cuando el usuario pida instalar, configurar o añadir **setup-roy** (o este repo) al proyecto actual.

### Reglas duras

- Destino del pack: `docs/setup-roy/` en la raíz del proyecto actual.
- Origen: **solo** el directorio `setup-roy/` de este repositorio.
- **No** copies al proyecto los docs de la raíz de este meta-repo (`README.md`, `INSTALL.md`, `bootstrap.py`) ni nada fuera de `setup-roy/`.
- No inventes rutas distintas (`setup/`, `.cursor/`, etc.) salvo que el usuario lo pida explícitamente.
- No hagas commit ni push como parte de la instalación salvo pedido explícito.

### Procedimiento preferido

Desde la **raíz del proyecto destino**. URL canónica: `https://github.com/roypm/setup-ia` (salvo que el usuario indique otra).

`bootstrap.py` no está en el proyecto destino: hay que obtenerlo (clone/zip temporal) y ejecutarlo desde la raíz del destino.

**Con git** (Linux/macOS o Git Bash):

```bash
git clone --depth 1 https://github.com/roypm/setup-ia /tmp/setup-ia
python3 /tmp/setup-ia/bootstrap.py --from /tmp/setup-ia
rm -rf /tmp/setup-ia
```

**Sin git** (Linux/macOS, con `curl` + `unzip` + Python):

```bash
curl -fsSL -o /tmp/setup-ia.zip https://github.com/roypm/setup-ia/archive/refs/heads/main.zip
unzip -q /tmp/setup-ia.zip -d /tmp
python3 /tmp/setup-ia-main/bootstrap.py --from /tmp/setup-ia-main
rm -rf /tmp/setup-ia.zip /tmp/setup-ia-main
```

**Con git** (Windows, PowerShell):

```powershell
git clone --depth 1 https://github.com/roypm/setup-ia $env:TEMP\setup-ia
python $env:TEMP\setup-ia\bootstrap.py --from $env:TEMP\setup-ia
Remove-Item -Recurse -Force $env:TEMP\setup-ia
```

**Sin git** (Windows, PowerShell + Python):

```powershell
Invoke-WebRequest -Uri https://github.com/roypm/setup-ia/archive/refs/heads/main.zip -OutFile $env:TEMP\setup-ia.zip
Expand-Archive $env:TEMP\setup-ia.zip -DestinationPath $env:TEMP -Force
python $env:TEMP\setup-ia-main\bootstrap.py --from $env:TEMP\setup-ia-main
Remove-Item -Recurse -Force $env:TEMP\setup-ia.zip, $env:TEMP\setup-ia-main
```

El script copia solo `setup-roy/` → `docs/setup-roy/` y actualiza `AGENTS.md`. Si el pack ya existe: `--force`. Para simular: `--dry-run`.

Si no puedes usar bootstrap (sin Python, sin red, etc.), haz el [fallback manual](#fallback-manual).

### Fallback manual

1. Obtén el contenido de `setup-roy/` desde el repo (clone temporal, descarga, o copia local).
2. Crea `docs/` si no existe.
3. Copia `setup-roy/` → `docs/setup-roy/`.
4. En `AGENTS.md` de la raíz: si ya existe el marcador `## Setup Roy`, no lo toques; si no, crea el archivo o haz append con el [snippet canónico](#snippet-canonico).
5. Borra temporales de descarga si los creaste.

### Verificación (obligatoria)

Confirma todo esto antes de dar la instalación por hecha:

- [ ] Existe `docs/setup-roy/agents.md` (índice del pack; el detalle de piezas vive ahí)
- [ ] `docs/setup-roy/` no está vacío y parece el pack (no solo un archivo suelto sin sentido)
- [ ] `AGENTS.md` en la raíz contiene el marcador `## Setup Roy` una sola vez
- [ ] No se copiaron al proyecto `README.md` / `INSTALL.md` / `bootstrap.py` de este meta-repo

### Respuesta al usuario

Resume en pocas líneas: rutas creadas/actualizadas, si el marcador era nuevo o ya estaba, y que el índice de uso es `docs/setup-roy/agents.md`.

---

## Opción humana

Misma meta que el contrato IA. Ejecuta los comandos desde la **raíz de tu proyecto**. Hace falta **Python 3** para `bootstrap.py`.

### Linux / macOS — con git

```bash
git clone --depth 1 https://github.com/roypm/setup-ia /tmp/setup-ia
python3 /tmp/setup-ia/bootstrap.py --from /tmp/setup-ia
rm -rf /tmp/setup-ia
```

### Linux / macOS — sin git

```bash
curl -fsSL -o /tmp/setup-ia.zip https://github.com/roypm/setup-ia/archive/refs/heads/main.zip
unzip -q /tmp/setup-ia.zip -d /tmp
python3 /tmp/setup-ia-main/bootstrap.py --from /tmp/setup-ia-main
rm -rf /tmp/setup-ia.zip /tmp/setup-ia-main
```

### Windows — con git (PowerShell)

```powershell
git clone --depth 1 https://github.com/roypm/setup-ia $env:TEMP\setup-ia
python $env:TEMP\setup-ia\bootstrap.py --from $env:TEMP\setup-ia
Remove-Item -Recurse -Force $env:TEMP\setup-ia
```

### Windows — sin git (PowerShell)

```powershell
Invoke-WebRequest -Uri https://github.com/roypm/setup-ia/archive/refs/heads/main.zip -OutFile $env:TEMP\setup-ia.zip
Expand-Archive $env:TEMP\setup-ia.zip -DestinationPath $env:TEMP -Force
python $env:TEMP\setup-ia-main\bootstrap.py --from $env:TEMP\setup-ia-main
Remove-Item -Recurse -Force $env:TEMP\setup-ia.zip, $env:TEMP\setup-ia-main
```

### Sin Python (cualquier SO)

1. Descarga el ZIP del repo: https://github.com/roypm/setup-ia/archive/refs/heads/main.zip  
   (o clona el repo si tienes git).
2. Copia la carpeta `setup-roy/` a `docs/setup-roy/` en tu proyecto (crea `docs/` si hace falta).
3. En la raíz, crea o edita `AGENTS.md` y pega el marcador y el [snippet canónico](#snippet-canonico) (sin duplicar nada).
4. Comprueba que existe `docs/setup-roy/agents.md`.
5. Borra el ZIP / clone temporal.

---

## Después de instalar

El índice y la lógica de piezas están en `docs/setup-roy/agents.md`. No hace falta releer este archivo para usar el pack.
