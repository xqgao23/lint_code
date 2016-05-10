#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : Given an integers array A
    @return :  an integer which is the first missing positive
    """
    def firstMissingPositive(self, A):
        if A == None or len(A) == 0:
            return 1
        
        length = len(A)
        positive_array = [1] * (length + 1)
        positive_array[0] = 0

        for i in A:
            if i > 0 and i <= length:
                positive_array[i] = 0

        min_positive = length + 1
        for i in range(length + 1):
            if positive_array[i] == 1:
                min_positive = i
                break

        return min_positive

if __name__ == "__main__":
    solution = Solution()
    if solution.firstMissingPositive([1, 2, 0]) == 3:
        print('test 1 pass')

    if solution.firstMissingPositive([3, 4, -1, 1]) == 2:
        print('test 2 pass')
