#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : a list of integers
    @return : an integer after remove duplicates elements.
    should not use extra array.
    """
    def removeDuplicates(self, A):
        if A == None:
            return 0

        total_length = len(A)
        length_left = total_length
        for i in range(total_length):
            while(True):
                if i + 1 >= length_left:
                    break
                
                if A[i] == A[i + 1]:
                    A.pop(i + 1)
                    length_left = length_left - 1
                else:
                    break
        return length_left
        

if __name__ == "__main__":
    solution = Solution()
    if solution.removeDuplicates([0, 0, 2, 2, 2, 4, 4, 4]) == 3:
        print("pass")