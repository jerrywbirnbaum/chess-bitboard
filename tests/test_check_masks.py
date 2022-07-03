from cmath import exp
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from move_generation.check_masks import *
import pytest


@pytest.mark.parametrize(
    "king_start, pawn_board, knight_board, bishop_board, rook_board, queen_board, color, expected",
    [
        (
            int("1", 2),
            int("1000000000", 2),
            0,
            0,
            0,
            0,
            "W",
            int("1000000000", 2),
        ),
        (
            int("10", 2),
            int("10100000000", 2),
            0,
            0,
            0,
            0,
            "W",
            int("10100000000", 2),
        ),
    ],
)
def test_check_mask(
    king_start,
    pawn_board,
    knight_board,
    bishop_board,
    rook_board,
    queen_board,
    color,
    expected,
):

    result = generate_check_mask(
        king_start,
        pawn_board,
        knight_board,
        bishop_board,
        rook_board,
        queen_board,
        color,
    )
    assert bin(result) == bin(expected)
