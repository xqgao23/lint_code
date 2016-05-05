#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : a list of integers
    @param elem: An integer
    @return : The new length after remove
    """
    def removeElement(self, A, elem):
        if A == None:
            return 0

        total_length = len(A)
        remove_count = 0
        for i in range(total_length):
            if A[i - remove_count] == elem:
                A.pop(i - remove_count)
                remove_count = remove_count + 1

        return total_length - remove_count
        

if __name__ == "__main__":
    solution = Solution()
    A = [0, 4, 4, 0, 0, 2, 4, 4]
    if solution.removeElement(A, 4) == 4:
        print(A)