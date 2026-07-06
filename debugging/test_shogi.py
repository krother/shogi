"""
Run the tests with

    uv run pytest

or

    pip install pytest
    pytest
"""
from shogi import start_game, execute_move


def test_move_lion():
    """lion moves"""
    field, player = start_game()

    move = (1, 0), (0, 1)
    field, player, winner = execute_move(field, player, move)

    assert field[1][0] == ("lion", 1)
    assert field[0][1] == ("", None)
    assert player == -1


def test_eat_chick():
    """chick gets eaten in the first move"""
    field, player = start_game()

    move = (1, 1), (1, 2)
    field, player, winner = execute_move(field, player, move)

    assert field[2][1] == ("chick", 1)
    assert player == -1


def test_eat_lion():
    """lion gets eaten in threen moves"""
    field, player = start_game()

    for move in [
        ((1, 0), (0, 1)),  # lion moves bottom-left
        ((1, 3), (0, 2)),  # other lion moves up-left
        ((0, 1), (0, 2)),  # eats!
    ]:
        field, player, winner = execute_move(field, player, move)

    assert winner == "top"
