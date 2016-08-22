#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param num: a rotated sorted array. the start of index is unknown. ie. [0, 1, 2, ..., 7] may be [4, 5, 6, 7, 0, 1]
    @return : the minimum number in the array
    """
    def findMin(self, num):
        if num == None:
            return 0

        length = len(num)
        max_index = length - 1
        min_index = 0
        min_num = num[0]

        while max_index >= min_index:
            target_index = int((max_index + min_index) / 2)
            if num[target_index] >= num[0]:
                min_index = target_index + 1
            else:
                min_num = num[target_index]
                max_index = target_index - 1

        return min_num


if __name__ == "__main__":
    solution = Solution()
    if solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0:
        print('test 1 pass')
    if solution.findMin([6, 1, 2, 3, 4, 5]) == 1:
        print('test 2 pass')