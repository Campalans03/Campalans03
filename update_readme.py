# update_readme.py
with open('README.md', 'r') as f:
    readme = f.read()

with open('game_board.txt', 'r') as f:
    game_board = f.read()

# Reemplazar la sección del tablero en el README
updated_readme = readme.replace('{{ game_board }}', game_board)

with open('README.md', 'w') as f:
    f.write(updated_readme)
