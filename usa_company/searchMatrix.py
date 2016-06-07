#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A: a list of sorted integers
    @param target: an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if A is None:
            return 0

        min_index = 0
        max_index = len(A) - 1
        result_index = 0

        while max_index >= min_index:
            result_index = int((min_index + max_index) / 2)
            if A[result_index] > target:
                max_index = result_index - 1
            elif A[result_index] < target:
                min_index = result_index + 1
            else:
                break

        if max_index < min_index:
            result_index = min_index

        return result_index


if __name__ == "__main__":
    solution = Solution()
    test_data = [1, 3, 5, 6]
    test_target = [5, 2, 7, 0]
    test_result = [2, 1, 4, 0]

    for i in range(len(test_target)):
        if solution.searchInsert(test_data, test_target[i]) == test_result[i]:
            print('test ', i + 1, ' pass')
