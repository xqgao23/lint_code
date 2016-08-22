#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A: a list of integers.  A sorted array. the start of index is unknown. ie. [0, 1, 2, ..., 7] may be [4, 5, 6, 7, 0, 1]
    @parma target: an integer to be searched
    @return : the index of the target if found else -1
    """
    def search(self, A, target):
        if A == None or len(A) == 0:
            return -1

        turn_index = self.get_min_index_of_array(A)

        length = len(A)
        max_index = length - 1
        min_index = 0
        target_index = 0

        if A[0] > target:
            min_index = turn_index
        elif A[0] < target:
            if turn_index != 0:
                max_index = turn_index - 1
        else:
            return 0

        while max_index >= min_index:
            mid_index = int((max_index + min_index) / 2)
            if A[mid_index] == target:
                return mid_index
            elif A[mid_index] > target:
                max_index = mid_index - 1
            else:
                min_index = mid_index + 1

        return -1

    def get_min_index_of_array(self, A):
        length = len(A)
        max_index = length - 1
        min_index = 0
        target_index  = 0

        while max_index >= min_index:
            mid_index = int((max_index + min_index) / 2)
            if A[mid_index] > A[0]:
                min_index = mid_index + 1
            else:
                target_index = mid_index
                max_index = mid_index - 1

        return target_index

if __name__ == "__main__":
    solution = Solution()
    if solution.search([4, 5, 1, 2, 3], 1) == 2:
        print('test 1 pass')
    if solution.search([4, 5, 1, 2, 3], 0) == -1:
        print('test 2 pass')
    if solution.search([0, 1, 2, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -9) == 4:
        print('test 3 pass')