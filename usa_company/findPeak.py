#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A: An inetegers list. if size == n.
            o. A[i] != A[i - 1]
            o. A[0] < A[1] and A[n - 2] > A[n - 1]
    @return : return any of peak positions.
    """
    def findPeak(self, A):
        if A == None:
            return 0

        if len(A) < 3:
            return 0

        peak_index = 1
        max_index = len(A) - 2
        min_index = 1

        while max_index >= min_index:
            mid_index = int((max_index + min_index) / 2)
            if self.is_peak_num(A, min_index):
                return min_index
            
            if A[mid_index - 1] < A[mid_index]:
                min_index = mid_index + 1
                peak_index = min_index
            else:
                max_index = mid_index - 1
                peak_index = mid_index - 1

        return peak_index

    def is_peak_num(self, A, index):
        if A[index] > A[index - 1] and A[index] > A[index + 1]:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    test1 = [4, 5, 6, 7, 0, 2, 1]
    if solution.findPeak(test1) == 3 or solution.findPeak(test1) == 5:
        print('test 1 pass')
    test2 = [1, 2, 1, 3, 4, 5, 7, 6]
    if solution.findPeak(test2) == 1 or solution.findPeak(test2) == 6:
        print('test 2 pass')