#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        if len(A) < len(B):
            return False

        a_list = list(A)
        try:
            for b in B:
                a_list.remove(b)
        except ValueError as e:
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    if solution.compareStrings('ABCD', 'ACD'):
        print('pass')

    if solution.compareStrings('ABCD', 'AABC'):
        print('fail')