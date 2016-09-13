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
                    a1 <= b1 <= c1 <= m1
    @param target: an integer to be found
    @return count of target in matrix
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return 0

        column_index = 0
        counts = 0
        columns = len(matrix)
        while column_index < columns and matrix[column_index][0] <= target:
            if self.target_in_row(matrix[column_index], target):
                counts = counts + 1
            column_index = column_index + 1

        return counts

    def target_in_row(self, row_array, target):
        min_index = 0
        max_index = len(row_array) - 1
        result_index = 0
        while max_index >= min_index:
            result_index = int((min_index + max_index) / 2 )
            if row_array[result_index] > target:
                max_index = result_index - 1
            elif row_array[result_index] < target:
                min_index = result_index + 1
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_data = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], [[1,3,5,7],[10,11,16,20],[23,30,34,50]], [[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]]]
    test_target = [3, 7, 3]
    test_result = [1, 1, 2]

    for i in range(len(test_target)):
        if solution.searchMatrix(test_data[i], test_target[i]) == test_result[i]:
            print('test ', i + 1, ' pass')
