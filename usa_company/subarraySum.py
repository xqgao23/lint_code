#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : a list of integers
    @param elem: An integer
    @return : The new length after remove
    """
    def subarraySum(self, nums):
        if nums == None:
            return []

        sums = 0

        for i in range(len(nums)):
            sums = nums[i]
            if sums == 0:
                return [i, i]
            for j in range(i + 1, len(nums)):
                sums = sums + nums[j]
                if sums == 0:
                    return [i, j]
        return []
        

if __name__ == "__main__":
    solution = Solution()
    if solution.subarraySum([-3, 1, 2, -3, 4]) == [0, 2] or solution.subarraySum([-3, 1, 2, -3, 4]) == [1, 3]:
        print('test 1 pass')