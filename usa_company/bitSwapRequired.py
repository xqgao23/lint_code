#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param a, b: Two integer
    return: An integer that nums of bit to change make A as B
    """
    def bitSwapRequired(self, a, b):
        swap_counts = 0

        a &= 0xffffffff
        b &= 0xffffffff
        while a != 0 or b != 0:
            if a % 2 != b % 2:
                swap_counts = swap_counts + 1
            a = int(a / 2)
            b = int(b / 2)

        return swap_counts

if __name__ == "__main__":
    solution = Solution()
    if solution.bitSwapRequired(31, 14) == 2:
        print("test 1 pass")

    if solution.bitSwapRequired(1, -1) == 31:
        print("test 2 pass")