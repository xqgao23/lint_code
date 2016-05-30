#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param numbers : Given an integers array numbers
    @param target: you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum equal to target.
    """
    def fourSum(self, numbers, target):
        if numbers == None or len(numbers) < 4:
            return []

        sum_array = []
        length = len(numbers)
        key_map = {}

        numbers = sorted(numbers)

        for i in range(length - 3):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            
            for j in range(i + 1, length - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue

                left = j + 1
                right = length - 1

                while right > left:
                    if left != j + 1 and numbers[left] == numbers[left - 1]:
                        left = left + 1
                        continue

                    if right != length - 1 and numbers[right] == numbers[right + 1]:
                        right = right - 1
                        continue

                    sums = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if sums < target:
                        left = left + 1
                    elif sums > target:
                        right = right - 1
                    else:
                        new_array = [numbers[i], numbers[j], numbers[left], numbers[right]]
                        key = self.array_to_key(new_array)
                        if key not in key_map:
                            sum_array.append(new_array)
                            key_map[key] = new_array
                        left = left + 1
                        right = right - 1

        return sum_array

    def array_to_key(self, a):
        key_value = 0
        for i in a:
            key_value = key_value * 10 + i
        return key_value

if __name__ == "__main__":
    solution = Solution()
    if solution.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]:
        print("test 1 pass")
    if solution.fourSum([1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,0,0,-2,2,-5,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99], 11) == [[-5,-2,6,12],[-5,0,8,8],[-5,1,3,12],[-5,1,7,8],[-5,2,2,12],[-5,2,6,8],[-5,2,7,7],[-5,3,5,8],[-5,3,6,7],[-5,5,5,6],[-2,0,1,12],[-2,0,5,8],[-2,0,6,7],[-2,1,5,7],[-2,1,6,6],[-2,2,3,8],[-2,2,5,6],[-2,3,3,7],[-2,3,5,5],[0,0,3,8],[0,0,5,6],[0,1,2,8],[0,1,3,7],[0,1,5,5],[0,2,2,7],[0,2,3,6],[0,3,3,5],[1,1,1,8],[1,1,2,7],[1,1,3,6],[1,2,2,6],[1,2,3,5],[2,2,2,5],[2,3,3,3]]:
        print('test 2 pass')