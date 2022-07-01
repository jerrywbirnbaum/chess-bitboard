from global_bitboards import CLEAR_FILE, FULL_BOARD
king_start = int('1000000000000000000000000000000000000000000000',2)
white_start = int('0000000000000000000000000000000000000000000000001111111111110111',2)

def compute_pseudo_king(king_loc, own_side):
    king_clip_file_h = king_loc & CLEAR_FILE['h']
    king_clip_file_a = king_loc & CLEAR_FILE['a']

    spot_1 = king_clip_file_h << 7
    spot_2 = king_loc << 8
    spot_3 = king_clip_file_h << 9
    spot_4 = king_clip_file_h << 1

    spot_5 = king_clip_file_a >> 7
    spot_6 = king_loc >> 8
    spot_7 = king_clip_file_a >> 9
    spot_8 = king_clip_file_a >> 1

    king_moves = spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 | spot_7 | spot_8



    king_moves = FULL_BOARD & king_moves
    king_moves = king_moves & ~own_side

    return king_moves


print(bin(compute_pseudo_king(king_start, white_start)))