from global_bitboards import CLEAR_FILE, FULL_BOARD

# king_start = int('1000000000000000000000000000000000000000000000',2)
# white_start = int('0000000000000000000000000000000000000000000000001111111111110111',2)


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
