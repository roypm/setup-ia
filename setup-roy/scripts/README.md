# Scripts (setup-roy)

Herramientas mecánicas: la IA (o tú) las ejecuta; no reinventar el flujo en prompts.

## `git_ship.py`

Commit + push eligiendo clave SSH y autor.

```bash
# Desde la raíz del proyecto (tras instalar el pack):
python docs/setup-roy/scripts/git_ship.py -m "mensaje del commit"

# Añadir paths, no pushear, simular:
python docs/setup-roy/scripts/git_ship.py -m "fix x" path/a path/b --no-push
python docs/setup-roy/scripts/git_ship.py -m "msg" --dry-run

# Sin prompts (CI / IA con datos ya elegidos):
python docs/setup-roy/scripts/git_ship.py -m "msg" --yes \
  --key ~/.ssh/id_ed25519_work \
  --name "Nombre" --email "tu@email"
```

Comportamiento:

1. Lista claves privadas en `~/.ssh/` (heurística: `id_*` / `ssh_*` o con `.pub` hermano).
2. Si hay varias, pregunta cuál usar (o exige `--key` con `--yes`).
3. Propone autor desde `git config user.*`; permite cambiarlo.
4. `git commit` con ese autor; `GIT_SSH_COMMAND` con la clave elegida.
5. `git push` a la upstream de la rama, o `git push -u origin <branch>` si no hay upstream.

Flags: `-m/--message`, `--key`, `--name`, `--email`, `--no-push`, `--dry-run`, `-y/--yes`, y paths opcionales para `git add`.
