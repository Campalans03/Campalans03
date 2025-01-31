# update_readme.py
import json

# Leer el README.md actual
with open('README.md', 'r') as f:
    readme = f.read()

# Leer el tablero del juego
with open('game_board.txt', 'r') as f:
    game_board = f.read()

# Leer el estado del juego
with open('game_state.json', 'r') as f:
    game_state = json.load(f)
    score = game_state["score"]

# Definir los marcadores de inicio y fin
start_marker = "<!-- GAME -->"
end_marker = "<!-- ENDGAME -->"

# Buscar la posición de los marcadores en el README.md
start_index = readme.find(start_marker)
end_index = readme.find(end_marker) + len(end_marker)

# Verificar si se encontraron los marcadores
if start_index == -1 or end_index == -1:
    raise ValueError("No se encontraron los marcadores <!-- GAME --> y <!-- ENDGAME --> en el README.md.")

# Plantilla para restaurar los marcadores
template = """
<!-- GAME -->
### Puntaje: {{ score }}

### Tablero:
<pre>
{{ game_board }}
</pre>
<!-- ENDGAME -->
"""

# Reemplazar la sección del juego con la plantilla que contiene los marcadores
updated_readme = readme[:start_index] + template + readme[end_index:]

# Escribir el README.md actualizado con la plantilla
with open('README.md', 'w') as f:
    f.write(updated_readme)

# Reemplazar los marcadores con los valores actuales
updated_readme = updated_readme.replace("{{ game_board }}", game_board)
updated_readme = updated_readme.replace("{{ score }}", str(score))

# Escribir el README.md final con los valores actualizados
with open('README.md', 'w') as f:
    f.write(updated_readme)
