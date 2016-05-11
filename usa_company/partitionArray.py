#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param num: The integer array you should partition
    @param k: As description
    @return :  The index after partition
    """
    def partitionArray(self, nums, k):
        if nums == None:
            return 0

        index = 0
        for i in range(len(nums)):
            if nums[i] < k:
                if index < i:
                    temp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = temp
                index = index + 1
        return index

if __name__ == "__main__":
    solution = Solution()
    if solution.partitionArray([3, 2, 2, 1], 2) == 1:
        print("test 1 pass")
    if solution.partitionArray([1, 2, 3, 3, 5, 5, 5, 4, 4, 7, 8], 3) == 2:
        print("test 2 pass")
