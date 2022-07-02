def print_bitboard(bitboard):
    str_board = bin(bitboard)[2:]
    padding = "0" * (64 - len(str_board))
    padded_board = padding + str_board

    print(padded_board[0:8])
    print(padded_board[8:16])
    print(padded_board[16:24])
    print(padded_board[24:32])
    print(padded_board[32:40])
    print(padded_board[40:48])
    print(padded_board[48:56])
    print(padded_board[56:])
