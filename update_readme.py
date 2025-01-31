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

# Reemplazar marcadores con los valores actuales
updated_readme = readme.replace('{{ game_board }}', game_board)
updated_readme = updated_readme.replace('{{ score }}', str(score))

# Escribir el README.md actualizado
with open('README.md', 'w') as f:
    f.write(updated_readme)

# Restaurar los marcadores específicos para la próxima ejecución
# Usamos una plantilla para restaurar solo los marcadores deseados
template = """
### Puntaje: {{ score }}

### Tablero:
<pre>
{{ game_board }}
</pre>
"""

# Buscamos la sección del tablero y el puntaje en el README.md actualizado
# y la reemplazamos con la plantilla que contiene los marcadores
start_marker = "### Puntaje: {{ score }}"
end_marker = "### Tablero:"

# Encontrar la posición de la sección del tablero y el puntaje
start_index = updated_readme.find(start_marker)
end_index = updated_readme.find(end_marker) + len(end_marker)

# Reemplazar solo la sección del tablero y el puntaje con la plantilla
restored_readme = (
    updated_readme[:start_index] + template + updated_readme[end_index:]
)

# Escribir el README.md con los marcadores restaurados
with open('README.md', 'w') as f:
    f.write(restored_readme)
