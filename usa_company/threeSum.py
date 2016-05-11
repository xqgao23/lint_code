#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param numbers : Given an integers array numbers
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if numbers == None or len(numbers) < 3:
            return []

        sum_array = []
        length = len(numbers)

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if numbers[i] + numbers[j] + numbers[k] == 0:
                        new_array = self.array_sort(numbers[i], numbers[j], numbers[k])
                        duplicate = False
                        for a in sum_array:
                            if a == new_array:
                                duplicate = True
                                break
                        if not duplicate:
                            sum_array.append(new_array)

        return sum_array

    def array_sort(self, i, j, k):
        if i < j:
            if k > j:
                return [i, j, k]
            elif k < i:
                return [k, i, j]
            else:
                return [i, k, j]
        else:
            if k > i:
                return [j, i, k]
            elif k < j:
                return [k, j, i]
            else:
                return [j, k, i]

if __name__ == "__main__":
    solution = Solution()
    if solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]:
        print("test 1 pass")
