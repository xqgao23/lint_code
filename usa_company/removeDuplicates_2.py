#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : a list of sorted integers
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
                if i + 2 >= length_left:
                    break
                
                if A[i] == A[i + 2]:
                    A.pop(i + 2)
                    length_left = length_left - 1
                else:
                    break
        return length_left
        

if __name__ == "__main__":
    solution = Solution()
    A = [1, 1, 1, 2, 2, 3]
    if solution.removeDuplicates(A) == 5:
        print(A)