#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if n <= 0:
            return False

        mask1 = 0x55555555
        mask2 = 0x33333333
        mask4 = 0x0f0f0f0f
        mask8 = 0x00ff00ff
        mask16 = 0x0000ffff

        n = (n & mask1) + ((n >> 1) & mask1)
        n = (n & mask2) + ((n >> 2) & mask2)
        n = (n & mask4) + ((n >> 4) & mask4)
        n = (n & mask8) + ((n >> 8) & mask8)
        n = (n & mask16) + ((n >> 16) & mask16)

        if n == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    if solution.checkPowerOf2(4) == True:
        print("test 1 pass")

    if solution.checkPowerOf2(5) == False:
        print("test 2 pass")