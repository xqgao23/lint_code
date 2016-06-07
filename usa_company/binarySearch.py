#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A: a list of sorted integers
    @param target: an integer to be found
    @return : the first position of target in nums, position start from 0
    """
    def binarySearch(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        min_index = 0
        max_index = len(nums) - 1
        result_index = 0

        while max_index >= min_index:
            result_index = int((min_index + max_index) / 2)
            if nums[result_index] > target:
                max_index = result_index - 1
            elif nums[result_index] < target:
                min_index = result_index + 1
            else:
                while result_index > min_index:
                    if nums[result_index - 1] != target:
                        break
                    else:
                        result_index = result_index - 1

                return result_index

        return -1

if __name__ == "__main__":
    solution = Solution()
    test_data = [[1, 2, 3, 3, 4, 5, 10]]
    test_target = [3]
    test_result = [2]

    for i in range(len(test_target)):
        if solution.binarySearch(test_data[i], test_target[i]) == test_result[i]:
            print('test ', i + 1, ' pass')
