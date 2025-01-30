import json
import sys

# Cargar el estado del juego
with open('game_state.json', 'r') as f:
    game_state = json.load(f)

# Obtener el movimiento del issue (pasado como argumento)
move = sys.argv[1].upper()

# Validar el movimiento
if move in ["UP", "DOWN", "LEFT", "RIGHT"]:
    # Actualizar la dirección del juego
    game_state["direction"] = move

    # Mover la serpiente
    head = game_state["snake"][0].copy()
    if move == "UP":
        head[1] -= 1
    elif move == "DOWN":
        head[1] += 1
    elif move == "LEFT":
        head[0] -= 1
    elif move == "RIGHT":
        head[0] += 1

    # Verificar colisiones
    if (head[0] < 0 or head[0] >= 20 or head[1] < 0 or head[1] >= 20 or
        head in game_state["snake"]):
        print("Game Over! Score:", game_state["score"])
        game_state["snake"] = [[10, 10], [10, 11], [10, 12]]
        game_state["food"] = [5, 5]
        game_state["direction"] = "RIGHT"
        game_state["score"] = 0
    else:
        game_state["snake"].insert(0, head)
        if head == game_state["food"]:
            game_state["score"] += 1
            game_state["food"] = [5, 5]  # Nueva posición de la comida (puedes randomizarla)
        else:
            game_state["snake"].pop()

    # Guardar el nuevo estado del juego
    with open('game_state.json', 'w') as f:
        json.dump(game_state, f, indent=2)

    # Generar representación ASCII del tablero
    board = [['·' for _ in range(20)] for _ in range(20)]
    for segment in game_state["snake"]:
        x, y = segment
        board[y][x] = '🟩'  # Cuerpo de la serpiente
    head_x, head_y = game_state["snake"][0]
    board[head_y][head_x] = '🟢'  # Cabeza de la serpiente
    food_x, food_y = game_state["food"]
    board[food_y][food_x] = '🍎'  # Comida

    # Guardar el tablero en un archivo de texto
    with open('game_board.txt', 'w') as f:
        for row in board:
            f.write(''.join(row) + '\n')
else:
    print("Movimiento no válido. Usa UP, DOWN, LEFT o RIGHT.")
