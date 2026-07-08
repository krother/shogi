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


def test_move_elephant():
    field, player = start_game()

    for move in [
        ((1, 1), (1, 2)),
        ((0, 3), (1, 2)),
    ]:
        field, player, _ = execute_move(field, player, move)

    print(field)
    assert field[2][1] == ("elephant", -1)
    assert field[3][0] == ("", None)
    assert player == 1


def test_move_giraffe():
    field, player = start_game()

    move = ((0, 0), (0, 1))
    field, player, _ = execute_move(field, player, move)

    assert field[1][0] == ("giraffe", 1)
    assert field[0][0] == ("", None)
    assert player == -1


def test_move_chick():
    """chicken moves"""
    field, player = start_game()

    move = (1, 1), (1, 2)
    assert field[1][1] == ("chick", 1)
    field, player, _ = execute_move(field, player, move)
    assert field[1][1] == ("", None)
    assert field[2][1] == ("chick", 1)
    assert player == -1


def test_eat_chick():
    """chick gets eaten in the first move"""
    field, player = start_game()

    move = (1, 1), (1, 2)
    field, player, _ = execute_move(field, player, move)

    assert field[2][1] == ("chick", 1)
    assert player == -1


def test_invalid_move_chick():
    field, player = start_game()

    move = (1, 1), (2, 2)
    field, player, winner = execute_move(field, player, move)
    assert field[2][2] == ("", None)
    assert player == 1


def test_eat_lion():
    """lion gets eaten in three moves"""
    field, player = start_game()

    for move in [
        ((1, 0), (0, 1)),  # lion moves bottom-left
        ((1, 3), (0, 2)),  # other lion moves up-left
        ((0, 1), (0, 2)),  # eats!
    ]:
        field, player, winner = execute_move(field, player, move)

    assert winner == "top"


def test_lion_reaches_bottom():
    """lion reaches other side in five moves"""
    field, player = start_game()

    for move in [
        ((1, 0), (0, 1)),  # lion moves bottom-left
        ((1, 3), (2, 2)),  # other lion moves up-right
        ((0, 1), (0, 2)),  # lion moves down once more
        ((2, 2), (2, 1)),  # other lion tries to catch up
        ((0, 2), (1, 3)),  # reaches bottom
    ]:
        field, player, winner = execute_move(field, player, move)

    assert winner == "top"


def test_convert_chick():
    field, player = start_game()

    for move in [
        ((1, 1), (1, 2)),
        ((1, 3), (0, 2)),
        ((1, 2), (1, 3)),
    ]:
        field, player, winner = execute_move(field, player, move)

    assert field[3][1] == ("chicken", 1)
