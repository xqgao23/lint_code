#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    """
    @param n and m: positive integer(1 <= n, m <= 1000)
    @return an integer
    """

    def uniquePaths(self, m, n):
        if m < 1 or n < 1:
            return 0
        
        self.max_paths = [[-1 for x in range(n + 1)] for y in range(m + 1)]
        self.m = m
        self.n = n
        return self.get_max_path(1 , 1)


    def get_max_path(self, r, c): 
        if r >= self.m or c >= self.n:
            return 1

        if self.max_paths[r][c] != -1:
            return self.max_paths[r][c]

        a = self.get_max_path(r + 1, c)
        b = self.get_max_path(r, c + 1)

        self.max_paths[r][c] = a + b
        return self.max_paths[r][c]


if __name__ == '__main__':
    solution = Solution()
    if solution.uniquePaths(0, 0) == 0:
        print("test case 1 pass.")
    if solution.uniquePaths(1, 1) == 1:
        print('test case 2 pass')
    if solution.uniquePaths(2, 3) == 3:
        print('test case 3 pass')
    if solution.uniquePaths(2, 62) == 62:
        print('test case 4 pass')
    if solution.uniquePaths(3, 80) == 3240:
        print('test case 5 pass')