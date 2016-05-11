#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param numbers : Given an integers array numbers
    @param target: target = numbers[index1] + numbers[index2]
    @return :  [index1 + 1, index2 + 1] whitch index1 < index2
    """
    def twoSum(self, numbers, target):
        if numbers == None or len(numbers) < 2:
            return []

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return []

if __name__ == "__main__":
    solution = Solution()
    if solution.twoSum([2, 7, 11, 15], 9) == [1, 2]:
        print("test 1 pass")
