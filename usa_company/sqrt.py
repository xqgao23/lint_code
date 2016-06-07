#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param x: An integer
    @return : The sqrt of x
    """
    def sqrt(self, x):
        min_num = 0
        max_num = x
        while max_num >= min_num:
            sqrt_num = int((min_num + max_num) / 2)
            test_num = sqrt_num * sqrt_num
            if test_num == x:
                return sqrt_num
            elif test_num > x:
                max_num = sqrt_num - 1
            else:
                min_num = sqrt_num + 1

        return max_num


if __name__ == "__main__":
    solution = Solution()
    if solution.sqrt(1) == 1:
        print("test 1 pass")
    if solution.sqrt(3) == 1:
        print("test 1 pass")
    if solution.sqrt(4) == 2:
        print('test 2 pass')

    if solution.sqrt(5) == 2:
        print('test 3 pass')

    if solution.sqrt(10) == 3:
        print('test 4 pass')
