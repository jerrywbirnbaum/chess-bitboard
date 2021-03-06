from cmath import exp
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from move_generation.pseudo_moves import *
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
        (
            int("1000000000000000000000000000000000000", 2),
            0,
            int("101000010001000000000001000100001010000000000000000000", 2),
        ),
        (int("1", 2), 0, int("100000010000000000", 2)),
        (
            int("1000000000000000000000000000000000000", 2),
            int("1000100001010000000000000000000", 2),
            int("101000010001000000000000000000000000000000000000000000", 2),
        ),
    ],
)
def test_knight_pseudo_moves(knight_start, same_side, expected):

    result = compute_pseudo_knight(knight_start, same_side)
    assert bin(result) == bin(expected)


@pytest.mark.parametrize(
    "white_pawn_start, all_pieces, black_pieces, expected",
    [
        (int("100000000", 2), 0, 0, int("1000000010000000000000000", 2)),
        (int("10000000000000000", 2), 0, 0, int("1000000000000000000000000", 2)),
        (
            int("100000000", 2),
            0,
            int("100000000000000000", 2),
            int("1000000110000000000000000", 2),
        ),
        (
            int("100000000", 2),
            int("1000000100000000000000000", 2),
            int("100000000000000000", 2),
            int("110000000000000000", 2),
        ),
    ],
)
def test_white_pawn_pseudo_moves(white_pawn_start, all_pieces, black_pieces, expected):

    result = compute_pseudo_white_pawn(white_pawn_start, all_pieces, black_pieces)
    assert bin(result) == bin(expected)


@pytest.mark.parametrize(
    "black_pawn_start, all_pieces, black_pieces, expected",
    [
        (
            int("1000000000000000000000000000000000000000000000000", 2),
            0,
            0,
            int("10000000100000000000000000000000000000000", 2),
        ),
    ],
)
def test_black_pawn_pseudo_moves(black_pawn_start, all_pieces, black_pieces, expected):

    result = compute_pseudo_black_pawn(black_pawn_start, all_pieces, black_pieces)
    assert bin(result) == bin(expected)


@pytest.mark.parametrize(
    "bishop_start, all_pieces, same_pieces, expected",
    [
        (
            int("0001000000000000000000000000000000000000000000000000000000000000", 2),
            int("1000000100100000000000000000001000000000000000000000000000000000", 2),
            int("1000000100100000000000000000001000000000000000000000000000000000", 2),
            int("0000000000001000000001000000000000000000000000000000000000000000", 2),
        ),
        (
            int("0000000000000000000000000001000000000000000000000000000000000000", 2),
            int("0000000000000100000000000000000000000000010000000000000000000000", 2),
            int("0000000000000100000000000000000000000000000000000000000000000000", 2),
            int("1000000001000000001010000000000000101000010001000000001000000001", 2),
        ),
        (
            int("0000010000000000000000000000000000000000000000000000000000000000", 2),
            int("0000000000000000000000010010000000000000000000000000000000000000", 2),
            int("0000000000000000000000010000000000000000000000000000000000000000", 2),
            int("0000000000001010000100000010000000000000000000000000000000000000", 2),
        ),
        (
            int("1", 2),
            int("0", 2),
            int("0", 2),
            int("1000000001000000001000000001000000001000000001000000001000000000", 2),
        ),
    ],
)
def test_bishop_pseudo_moves(bishop_start, all_pieces, same_pieces, expected):

    result = compute_pseudo_bishop(bishop_start, all_pieces, same_pieces)
    breakpoint
    assert bin(result) == bin(expected)


@pytest.mark.parametrize(
    "rook_start, all_pieces, same_pieces, expected",
    [
        (
            int("1", 2),
            0,
            0,
            int("0000000100000001000000010000000100000001000000010000000111111110", 2),
        ),
    ],
)
def test_rook_pseudo_moves(rook_start, all_pieces, same_pieces, expected):

    result = compute_pseudo_rook(rook_start, all_pieces, same_pieces)
    breakpoint
    assert bin(result) == bin(expected)


@pytest.mark.parametrize(
    "queen_start, all_pieces, same_pieces, expected",
    [
        (
            int("1", 2),
            0,
            0,
            int("1000000101000001001000010001000100001001000001010000001111111110", 2),
        ),
    ],
)
def test_queen_pseudo_moves(queen_start, all_pieces, same_pieces, expected):

    result = compute_pseudo_queen(queen_start, all_pieces, same_pieces)
    assert bin(result) == bin(expected)
