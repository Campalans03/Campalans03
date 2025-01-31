with open('README.md', 'r') as f:
    readme = f.read()

with open('game_board.txt', 'r') as f:
    game_board = f.read()

with open('game_state.json', 'r') as f:
    game_state = json.load(f)
    score = game_state["score"]

# Reemplazar marcadores
updated_readme = readme.replace('{{ game_board }}', game_board)
updated_readme = updated_readme.replace('{{ score }}', str(score))

with open('README.md', 'w') as f:
    f.write(updated_readme)
