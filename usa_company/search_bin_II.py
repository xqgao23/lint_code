#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A: a list of integers.  A sorted array and duplicates are. the start of index is unknown. ie. [0, 1, 2, ..., 7] may be [4, 5, 6, 7, 0, 1]
    @parma target: an integer to be searched
    @return : the index of the target if found else -1
    """
    def search(self, A, target):
        if A == None or len(A) == 0:
            return False

        turn_index = self.get_min_index_of_array(A, 0)

        length = len(A)
        max_index = length - 1
        min_index = 0
        target_index = 0

        if A[0] > target:
            min_index = turn_index
        elif A[0] < target:
            if turn_index != 0:
                max_index = turn_index - 1
        else:
            return True

        while max_index >= min_index:
            mid_index = int((max_index + min_index) / 2)
            if A[mid_index] == target:
                return True
            elif A[mid_index] > target:
                max_index = mid_index - 1
            else:
                min_index = mid_index + 1

        return False

    def get_min_index_of_array(self, num, start_index):
        if num == None:
            return 0

        length = len(num)
        max_index = length - 1
        min_index = 0
        min_target_index = 0

        while max_index >= min_index:
            target_index = int((max_index + min_index) / 2)
            if num[target_index] > num[0]:
                min_index = target_index + 1
            elif num[target_index] < num[0]:
                min_target_index = target_index
                max_index = target_index - 1
            else:
                if target_index == 0:
                    min_index = target_index + 1
                else:
                    front_min_index = self.get_min_index_of_array(num[:target_index], 0)
                    end_min_index = self.get_min_index_of_array(num[target_index:], target_index)

                    if num[front_min_index] > num[end_min_index]:
                        return end_min_index
                    else:
                        return front_min_index
        return min_target_index + start_index


if __name__ == "__main__":
    solution = Solution()
    if solution.search([4, 5, 1, 2, 3], 1) == True:
        print('test 1 pass')
    if solution.search([4, 5, 1, 2, 3], 0) == False:
        print('test 2 pass')
    if solution.search([0, 1, 2, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -9) == True:
        print('test 3 pass')
    if solution.search([3, 4, 4, 5, 7, 0, 1, 2], 4) == True:
        print('test 4 pass')
    if solution.search([9, 5, 6, 7, 8, 9, 9, 9, 9, 9], 8) == True:
        print('test 5 pass')
    if solution.search([2, 2, 2, 3, 1], 1) == True:
        print('test 6 pass')

