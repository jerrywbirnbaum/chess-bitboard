from gmpy2 import bit_scan1
import numpy as np


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


# print(bin((99 | 2**64)))
# print(bit_scan1((99 | 2**64),2))


def reverse_bits(n, no_of_bits):
    result = 0
    for i in range(no_of_bits):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result


def bitscan_reverse(num):
    if num == 0:
        return 63
    num |= 2**64
    num <<= 1
    num |= 1
    num = reverse_bits(num, 66)
    return bit_scan1(num, 1) - 1


def bitscan_forward(num):
    scan_num = bit_scan1(num)
    if scan_num:
        return 63 - scan_num
    else:
        return 0


print(bitscan_reverse(2**63))
