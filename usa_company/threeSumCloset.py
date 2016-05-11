#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param numbers : Given an integers array numbers
    @param target: An integer
    @return : return the sum of the three integer, the sum closest target
    """
    def threeSumCloset(self, numbers, target):
        if numbers == None or len(numbers) < 3:
            return 0

        closet_abs = 0x7FFFFFFF
        min_sum = 0
        length = len(numbers)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    new_sum = numbers[i] + numbers[j] + numbers[k]
                    new_closet_abs = new_sum - target if new_sum > target else target - new_sum
                    if new_closet_abs < closet_abs:
                        closet_abs = new_closet_abs
                        min_sum = new_sum

        return min_sum


if __name__ == "__main__":
    solution = Solution()
    if solution.threeSumCloset([-1, 2, 1, -4], 1) == 2:
        print("test 1 pass")
