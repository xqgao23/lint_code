#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : Given an integers array A
    @return :  An integer array B and B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        if A == None or len(A) == 0:
            return []
        
        B = []

        for i in range(len(A)):
            result = self.get_products_excluse(A, i)
            B.append(result)

        return B

    def get_products_excluse(self, A, index):
        result = 1
        for i in range(len(A)):
            if i == index:
                continue
            result = result * A[i]
        return result

if __name__ == "__main__":
    solution = Solution()
    if solution.productExcludeItself([1, 2, 3]) == [6, 3, 2]:
        print('test 1 pass')

