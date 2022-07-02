from itertools import chain
from helpers import print_bitboard
from functools import lru_cache


def generate_diagonal_rays(rays, start_row, start_col):
    index = start_row * 8 + start_col
    rays[index] = {}

    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col

    # northwest
    while count_row >= 0 and count_col >= 0:
        board[count_row][count_col] = 1
        count_row -= 1
        count_col -= 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)

    rays[index]["NW"] = int(out_board, 2)

    # northeast
    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col
    while count_row >= 0 and count_col < 8:
        board[count_row][count_col] = 1
        count_row -= 1
        count_col += 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)
    rays[index]["NE"] = int(out_board, 2)

    # southwest
    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col
    while count_row < 8 and count_col >= 0:
        board[count_row][count_col] = 1
        count_row += 1
        count_col -= 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)
    rays[index]["SW"] = int(out_board, 2)

    # southeast
    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col
    while count_row < 8 and count_col < 8:
        board[count_row][count_col] = 1
        count_row += 1
        count_col += 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)
    rays[index]["SE"] = int(out_board, 2)

    return rays


def generate_straight_rays(rays, start_row, start_col):
    index = start_row * 8 + start_col
    rays[index] = {}

    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col

    # north
    while count_row >= 0:
        board[count_row][count_col] = 1
        count_row -= 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)

    rays[index]["N"] = int(out_board, 2)

    # South
    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col
    while count_row < 8:
        board[count_row][count_col] = 1
        count_row += 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)
    rays[index]["S"] = int(out_board, 2)

    # west
    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col
    while count_col >= 0:
        board[count_row][count_col] = 1
        count_col -= 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)
    rays[index]["W"] = int(out_board, 2)

    # east
    board = [[0] * 8 for _ in range(8)]
    count_row = start_row
    count_col = start_col
    while count_col < 8:
        board[count_row][count_col] = 1
        count_col += 1
    board[start_row][start_col] = 0

    flattented_board = list(chain.from_iterable(board))
    out_board = ""
    for num in flattented_board:
        out_board += str(num)
    rays[index]["E"] = int(out_board, 2)

    return rays


def all_diagonal_rays():
    rays = {}
    for i in range(8):
        for j in range(8):
            generate_diagonal_rays(rays, i, j)

    return rays


def all_straight_rays():
    rays = {}
    for i in range(8):
        for j in range(8):
            generate_straight_rays(rays, i, j)

    return rays
