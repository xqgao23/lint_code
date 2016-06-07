#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param matrix: a list of listed of sorted integers.
                    [
                        [a1, a2, a3, ... an],
                        [b1, b2, b3, ... bn],
                        [c1, c2, c3, ... cn]
                    ]
                    a1 <= a2 <= a3 ... <= an
                    an <= b1 <= bn <= c1 <= cn
    @param target: an integer to be found
    @return a boolen, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return False

        min_index = 0
        max_index = len(matrix) - 1
        result_index = 0

        while max_index >= min_index:
            result_index = int((min_index + max_index) / 2)
            if matrix[result_index][0] > target:
                max_index = result_index - 1
            elif matrix[result_index][0] < target:
                min_index = result_index + 1
            else:
                break

        if max_index < min_index:
            result_index = max_index

        min_index = 0
        max_index = len(matrix[result_index]) - 1
        new_result_index = 0
        while max_index >= min_index:
            new_result_index = int((min_index + max_index) / 2)
            if matrix[result_index][new_result_index] > target:
                max_index = new_result_index - 1
            elif matrix[result_index][new_result_index] < target:
                min_index = new_result_index + 1
            else:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    test_data = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], [[1,3,5,7],[10,11,16,20],[23,30,34,50]]]
    test_target = [3, 7]
    test_result = [True, True]

    for i in range(len(test_target)):
        if solution.searchMatrix(test_data[i], test_target[i]) == test_result[i]:
            print('test ', i + 1, ' pass')
