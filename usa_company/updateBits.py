#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    # @param n, m: Two integer
    # @param i, j: Two bit positions
    # return: An integer
    def updateBits(self, n, m, i, j):
        if j == 31:
            t1 = (n & 0xFFFFFFFF) & (~(0xFFFFFFFF << i) | (0xFFFFFFFF << (j + 1))) | (m << i)
            if t1 >> 31 == 1:
                t1 = (t1 & 0x7FFFFFFF) - (1 << 31)
            return t1
        else:
            return n & (~(0xFFFFFFFF << i) | (0xFFFFFFFF << (j + 1))) | (m << i)
            

if __name__ == '__main__':
    solution = Solution()
    if solution.updateBits(0b10000000000, 0b10101, 2, 6) == 0b10001010100:
        print('test 1 pass')

    if solution.updateBits(-521, 0, 31, 31) == 2147483127:
        print('test 2 pass')

    if solution.updateBits(1, -1, 0, 31) == -1:
        print('test 3 pass')
    
    if solution.updateBits(1, 1, 0, 31) == 1:
        print('test 4 pass')

    if solution.updateBits(-2147483648, 2147483647, 0, 30) == -1:
        print('test 5 pass')
    
    if solution.updateBits(456, 31, 27, 31) == -134217272:
        print('test 6 pass')