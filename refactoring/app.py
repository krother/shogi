"""
Minimal REST API for Dōbutsu shōgi
- a tactical kids game from Japan

run with:

    uv sync
    uv run fastapi run --reload app.py

or

    pip install fastapi[standard]
    fastapi run --reload app.py

then visit localhost:3000 in your browser
"""
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from shogi import execute_move, start_game

BASE_DIR = Path(__file__).parent.parent

app = FastAPI(title="Dōbutsu shōgi API")

games = {}


class Move(BaseModel):
    from_x: int
    from_y: int
    to_x: int
    to_y: int


def game_state(game_id):
    field, player, winner = games[game_id]
    return {"game_id": game_id, "field": field, "player": player, "winner": winner}


@app.post("/games")
def new_game():
    field, player = start_game()
    game_id = str(uuid4())
    games[game_id] = (field, player, None)
    return game_state(game_id)


@app.get("/games/{game_id}")
def get_game(game_id: str):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="game not found")
    return game_state(game_id)


@app.post("/games/{game_id}/moves")
def make_move(game_id: str, move: Move):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="game not found")

    field, player, winner = games[game_id]
    if winner:
        raise HTTPException(status_code=400, detail="game is already over")

    for x, y in ((move.from_x, move.from_y), (move.to_x, move.to_y)):
        if not (0 <= x < 3 and 0 <= y < 4):
            raise HTTPException(status_code=400, detail="coordinates out of range")

    coords = ((move.from_x, move.from_y), (move.to_x, move.to_y))

    field, player, winner = execute_move(field, player, coords)
    games[game_id] = (field, player, winner)
    return game_state(game_id)


# serves index.html and the piece .svg files from the project root
app.mount("/", StaticFiles(directory=BASE_DIR, html=True), name="static")
