"""
Dōbutsu shōgi

a tactical kids game from Japan

run with:

    uv sync
    uv run fastapi run --reload app.py

or

    pip install fastapi[standard]
    fastapi run --reload app.py

then visit localhost:3000 in your browser

For a command line interface simply execute shogi.py.
"""
MOVE_CHARS = "abcdefghijkl"


def draw(field):
    """prints the playing field"""
    chars = iter(MOVE_CHARS)
    for row in field:
        print("-" * 39)
        print()
        s = ""
        for piece, direction in row:
            c = next(chars)
            if piece and direction == -1:
                piece = piece.upper()            
            piece += f" [{c}]"
            s += f"{piece:^13}"
        print(s)
        print()
    print("-" * 39)


def enter_move(player):
    """asks current player to enter the start and end square of a move"""
    print("top players turn" if player == 1 else "BOTTOM players turn")

    # enter move
    move_from = input("move from: ")
    move_to = input("move to: ")

    # convert move to coordinates
    move_from_idx = MOVE_CHARS.index(move_from)
    start_x = move_from_idx % 3
    start_y = move_from_idx // 3

    move_to_idx = MOVE_CHARS.index(move_to)
    end_x = move_to_idx % 3
    end_y = move_to_idx // 3

    return (start_x, start_y), (end_x, end_y)

def execute_move(field, player, move):
    winner = None

    (start_x, start_y), (end_x, end_y) = move

    # check if piece belongs to player
    valid = False
    if field[start_y][start_x][1] == player:
        # check if the target is empty or opponent
        if field[end_y][end_x][1] is None or field[end_y][end_x][1] == -player:
            # check if move is valid
            dx = end_x - start_x
            dy = end_y - start_y
            piece = field[start_y][start_x][0]
            if piece == "lion":
                # moves in all directions
                if abs(dx) == 1 or abs(dy) == 1:
                    valid = True
            elif piece == "elephant":
                # moves diagonally
                if abs(dx) == 1 and abs(dy) == 1:
                    valid = True
            elif piece == "giraffe":
                # moves along axes
                if abs(dx) + abs(dy) == 1 and max(abs(dx), abs(dy)) == 1:
                    valid = True
            elif piece == "chick":
                # only moves forward
                if dx == 0 and dy == player:
                    valid = True
            elif piece == "chicken":
                # moves everywhere but diagonally backwards
                if (dx, dy) in [(-1, 0), (1, 0), (-1, player), (0, player), (1, player), (0, -player)]:
                    valid = True
        
    # apply valid move
    if valid:

        # check for win
        eaten = field[end_y][end_x][0]
        if eaten == "lion":
            winner = "top" if player==1 else "bottom"

        # move piece
        field[end_y][end_x] = field[start_y][start_x]
        field[start_y][start_x] = "", None

        # next players turn
        player *= -1

        # upgrade chick -> chicken when it reaches last row
        if field[end_y][end_x][0] == "chick" and end_y in (0, 3):
            field[end_y][end_x] = ("chicken", "player")

    else:
        print("\ninvalid move!\n")

    # check if lion reached opposite row
    top_row = field[0]
    for piece, direction in top_row:
        if piece == "lion" and direction == -1:
            winner = "bottom"
    bottom_row = field[-1]
    for piece, direction in bottom_row:
        if piece == "lion" and direction == 1:
            winner = "top"
    
    return field, player, winner

def start_game():
    """creates the playing field"""
    field = [
        [("giraffe", 1), ("lion", 1), ("elephant", 1)],
        [("", None), ("chick", 1), ("", None)],
        [("", None), ("chick", -1), ("", None)],
        [("elephant", -1), ("lion", -1), ("giraffe", -1)],
    ]
    player = 1

    return field, player
    

def cli_game():
    """runs the game in a text terminal"""
    field, player = start_game()

    winner = None
    while not winner:
        draw(field)
        move = enter_move(player)
        field, player, winner = execute_move(field, player, move)

    print("winner:", winner)


if __name__ == "__main__":
    cli_game()
