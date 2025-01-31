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

# Restaurar los marcadores para la próxima ejecución
restored_readme = updated_readme.replace(game_board, '{{ game_board }}')
restored_readme = restored_readme.replace(str(score), '{{ score }}')

# Escribir el README.md con los marcadores restaurados
with open('README.md', 'w') as f:
    f.write(restored_readme)
