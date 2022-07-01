import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from pseudo_moves import *
import pytest


@pytest.mark.parametrize(
    "king_start, same_side, expected",
    [
        (int("1000", 2), int("1111111111110111", 2), 0),
        (
            int("1000000000000000000000000000000000000000000000000000000000000000", 2),
            int("0", 2),
            int("0100000011000000000000000000000000000000000000000000000000000000", 2),
        ),
        (int("1", 2), int("0", 2), int("1100000010", 2)),
        (int("1000000000000000000", 2), 0, int("1110000010100000111000000000", 2)),
    ],
)
def test_king_pseudo_moves(king_start, same_side, expected):

    result = compute_pseudo_king(king_start, same_side)
    assert bin(result) == bin(expected)

@pytest.mark.parametrize(
    "knight_start, same_side, expected",
    [
        (int("1000000000000000000000000000000000000", 2), 0, int("101000010001000000000001000100001010000000000000000000", 2)),
        (int("1", 2), 0, int("100000010000000000", 2)),
        (int("1000000000000000000000000000000000000", 2), int("1000100001010000000000000000000", 2), int("101000010001000000000000000000000000000000000000000000", 2)),
    ],
)
def test_knight_pseudo_moves(knight_start, same_side, expected):

    result = compute_pseudo_knight(knight_start, same_side)
    assert bin(result) == bin(expected)
