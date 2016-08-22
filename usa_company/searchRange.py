#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
     """
     @param A: a list of sorted integers.
     @param target: an integer to be searched
     @return: a list of length 2, [index1, index2]
     """

     def searchRange(self, A, target):
        if A == None or len(A) == 0:
            return [-1, -1]

        max_index = len(A) - 1
        min_index = 0
        start_index = -1
        end_index = -1

        while max_index >= min_index:
            mid_index = int((max_index + min_index) / 2)
            if A[mid_index] == target:
                start_index = mid_index
                end_index = mid_index
                break
            elif A[mid_index] > target:
                max_index = mid_index - 1
            else:
                min_index = mid_index + 1

        if start_index == -1:
            return [-1, -1]

        new_max_index = start_index - 1
        new_min_index = min_index
        while new_max_index >= new_min_index:
            mid_index = int((new_max_index + new_min_index) / 2)
            if A[mid_index] == target:
                start_index = mid_index
                new_max_index = mid_index - 1
            else:
                new_min_index = mid_index + 1

        new_max_index = max_index
        new_min_index = end_index + 1
        while new_max_index >= new_min_index:
            mid_index = int((new_min_index + new_max_index) / 2)
            if A[mid_index] == target:
                end_index = mid_index
                new_min_index = mid_index + 1
            else:
                new_max_index = mid_index - 1

        return [start_index, end_index]

if __name__ == "__main__":
    solution = Solution()
    if solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]:
        print('test 1 pass')