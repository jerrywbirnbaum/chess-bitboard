from global_bitboards import CLEAR_FILE, FULL_BOARD, MASK_RANK
from generate_rays import all_diagonal_rays, all_straight_rays
from helpers import print_bitboard, bitscan_forward, bitscan_reverse

DIAGONAL_RAYS = all_diagonal_rays()
STRAIGHT_RAYS = all_straight_rays()


def compute_pseudo_king(king_loc, own_side):
    king_loc = king_loc & FULL_BOARD
    king_clip_file_h = king_loc & CLEAR_FILE["h"]
    king_clip_file_a = king_loc & CLEAR_FILE["a"]

    spot_1 = king_clip_file_h << 7
    spot_2 = king_loc << 8
    spot_3 = king_clip_file_a << 9
    spot_4 = king_clip_file_a << 1

    spot_5 = king_clip_file_a >> 7
    spot_6 = king_loc >> 8
    spot_7 = king_clip_file_h >> 9
    spot_8 = king_clip_file_h >> 1

    king_moves = spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 | spot_7 | spot_8

    king_moves = FULL_BOARD & king_moves
    king_moves = king_moves & ~own_side

    return king_moves


def compute_pseudo_knight(knight_loc, own_side):
    knight_loc = knight_loc & FULL_BOARD
    knight_clip_file_a = knight_loc & CLEAR_FILE["a"]
    knight_clip_file_h = knight_loc & CLEAR_FILE["h"]
    knight_clip_file_ab = knight_loc & CLEAR_FILE["a"] & CLEAR_FILE["b"]
    knight_clip_file_gh = knight_loc & CLEAR_FILE["g"] & CLEAR_FILE["h"]

    spot_1 = knight_clip_file_ab << 10
    spot_2 = knight_clip_file_ab >> 6

    spot_3 = knight_clip_file_a << 17
    spot_4 = knight_clip_file_a >> 15

    spot_5 = knight_clip_file_h << 15
    spot_6 = knight_clip_file_h >> 17

    spot_7 = knight_clip_file_gh << 6
    spot_8 = knight_clip_file_gh >> 10

    knight_moves = spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 | spot_7 | spot_8

    knight_moves = FULL_BOARD & knight_moves
    knight_moves = knight_moves & ~own_side

    return knight_moves


def compute_pseudo_white_pawn(pawn_loc, all_pieces, black_pieces):
    pawn_one_step = (pawn_loc << 8) & ~all_pieces
    pawn_two_step = ((pawn_one_step & MASK_RANK["3"]) << 8) & ~all_pieces

    pawn_moves = pawn_one_step | pawn_two_step

    pawn_left_attack = (pawn_loc & CLEAR_FILE["a"]) << 9
    pawn_right_attack = (pawn_loc & CLEAR_FILE["h"]) << 7
    pawn_attacks = (pawn_left_attack | pawn_right_attack) & black_pieces

    pawn_moves_and_attacks = pawn_moves | pawn_attacks
    return pawn_moves_and_attacks


def compute_pseudo_black_pawn(pawn_loc, all_pieces, white_pieces):
    pawn_one_step = (pawn_loc >> 8) & ~all_pieces
    pawn_two_step = ((pawn_one_step & MASK_RANK["6"]) >> 8) & ~all_pieces

    pawn_moves = pawn_one_step | pawn_two_step

    pawn_left_attack = (pawn_loc & CLEAR_FILE["a"]) >> 7
    pawn_right_attack = (pawn_loc & CLEAR_FILE["h"]) >> 9
    pawn_attacks = (pawn_left_attack | pawn_right_attack) & white_pieces

    pawn_moves_and_attacks = pawn_moves | pawn_attacks
    return pawn_moves_and_attacks


def compute_pseudo_bishop(bishop_loc, all_pieces, same_pieces, rays=DIAGONAL_RAYS):
    bishop_idx = bitscan_reverse(bishop_loc)
    bishop_moves = 0
    for key, value in rays[bishop_idx].items():
        bishop_ray = value
        if key in ["NE", "NW"]:
            blocker_index = bitscan_forward(bishop_ray & all_pieces)
        else:
            blocker_index = bitscan_reverse(bishop_ray & all_pieces)
        blocker_ray = rays[blocker_index][key]
        bishop_moves |= bishop_ray & ~blocker_ray

    bishop_moves &= ~same_pieces

    return bishop_moves


def compute_pseudo_rook(rook_loc, all_pieces, same_pieces, rays=STRAIGHT_RAYS):
    rook_idx = bitscan_reverse(rook_loc)
    rook_moves = 0
    for key, value in rays[rook_idx].items():
        rook_ray = value
        if key in ["N", "W"]:
            blocker_index = bitscan_forward(rook_ray & all_pieces)
        else:
            blocker_index = bitscan_reverse(rook_ray & all_pieces)
        blocker_ray = rays[blocker_index][key]
        rook_moves |= rook_ray & ~blocker_ray

    rook_moves &= ~same_pieces

    return rook_moves


def compute_pseudo_queen(queen_loc, all_pieces, same_pieces):
    bishop_moves = compute_pseudo_bishop(queen_loc, all_pieces, same_pieces)
    rook_moves = compute_pseudo_rook(queen_loc, all_pieces, same_pieces)
    return bishop_moves | rook_moves
