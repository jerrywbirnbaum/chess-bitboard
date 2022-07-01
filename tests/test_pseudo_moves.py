import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from pseudo_moves import compute_pseudo_king
import pytest

@pytest.mark.parametrize("king_start, same_side, expected",
    [
        (int('1000',2), int('1111111111110111',2), 0),
        (int('1000000000000000000000000000000000000000000000000000000000000000',2),
        int('0',2),
        int('01000000110000000000000000000000000000000000000000000000000000000',2)),
    ]
)
def test_king_pseudo_moves(king_start, same_side, expected):
    # king_start = int('0000000000000000000000000000000000000000001000',2)
    # white_start = int('0000000000000000000000000000000000000000000000001111111111110111',2)
    # expected = 0
    result = compute_pseudo_king(king_start, same_side)
    assert bin(result) == bin(expected)

