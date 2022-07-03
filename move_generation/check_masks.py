from sre_constants import CH_LOCALE
from global_bitboards import FULL_BOARD, CLEAR_FILE


def generate_check_mask(
    king_pos, pawn_board, knight_board, bishop_board, rook_board, queen_board, color
):
    in_check = False
    check_mask = 0

    # PAWN checks
    pawn_right_attack = 0
    pawn_left_attack = 0

    if color == "B":
        pawn_left_attack = (pawn_board & CLEAR_FILE["a"]) << 9
        pawn_right_attack = (pawn_board & CLEAR_FILE["h"]) << 7

        if pawn_left_attack & king_pos != 0:
            check_mask |= king_pos >> 9
        if pawn_right_attack & king_pos != 0:
            check_mask |= king_pos >> 7
    else:
        pawn_left_attack = (pawn_board & CLEAR_FILE["a"]) >> 7
        pawn_right_attack = (pawn_board & CLEAR_FILE["h"]) >> 9

        if pawn_left_attack & king_pos != 0:
            check_mask |= king_pos << 7
        if pawn_right_attack & king_pos != 0:
            check_mask |= king_pos << 9

    if check_mask:
        return check_mask
    else:
        return FULL_BOARD
