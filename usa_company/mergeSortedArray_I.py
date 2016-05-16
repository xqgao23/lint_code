#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : sorted integer array A
    @param B : sorted integer array B.
    @return : A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        result = []
        length_of_A = len(A)
        length_of_B = len(B)
        index_in_B = 0
        for i in range(length_of_A):
            for j in range(index_in_B, length_of_B):
                if A[i] < B[j]:
                    break
                result.append(B[j])
                index_in_B = j + 1

            result.append(A[i])

        for j in range(index_in_B, length_of_B):
            result.append(B[j])
        
        return result

if __name__ == "__main__":
    solution = Solution()
    if solution.mergeSortedArray([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]:
        print('test 1 pass')
    A = [1, 2, 3]
    if solution.mergeSortedArray(A, [1, 2]) == [1, 1, 2, 2, 3]:
        print('test 2 pass')
    A = []
    if solution.mergeSortedArray(A, [1, 2]) == [1, 2]:
        print('test 3 pass')