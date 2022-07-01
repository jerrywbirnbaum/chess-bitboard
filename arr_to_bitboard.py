starting_position = "rnbqkbnrpppppppp00000000000000000000000000000000PPPPPPPPRNBQKBNR"


def bitLen(int_type):
    length = 0
    while int_type:
        int_type >>= 1
        length += 1
    return length


def string_to_bitboards(position):
    bitboards = []
    pieces = ["p", "r", "n", "b", "q", "k", "P", "R", "N", "B", "Q", "K"]
    for i, char in enumerate(pieces):
        board = position

        other_pieces = pieces.copy()
        current_piece = other_pieces.pop(i)

        board = board.replace(current_piece, "1")
        for other_piece in other_pieces:
            board = board.replace(other_piece, "0")

        bitboards.append(int(board, 2))

    return bitboards


bitboards = string_to_bitboards(starting_position)

print(bin(bitboards[-1]))
