#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : A string
    @param B : B string
    @return :  return the max common string in A and B string
    """
    def longestCommonSubstring(self, A, B):
        if A == None or B == None:
            return 0

        if len(A) == 0 or len(B) == 0:
            return 0

        source_string = ""
        target_string = ""
        longest_common_string = 0

        if len(A) > len(B):
            target_string = A
            source_string = B
        else:
            target_string = B
            source_string = A

        for i in range(len(source_string)):
            if longest_common_string >= len(source_string) - i:
                break;

            while True:
                if longest_common_string >= len(source_string) - i:
                    break;

                compare_str = source_string[i:i + longest_common_string + 1]
                if self.isSourceInTarget(target_string, compare_str) >= 0:
                    longest_common_string = longest_common_string + 1
                else:
                    break

        return longest_common_string

    def isSourceInTarget(self, source, target):
        s_list = list(source)
        t_list = list(target)
        for i in range(len(source) - 1):
            j = 0
            while j != len(target):            
                if i + j == len(source):
                    break;

                if s_list[i + j] != t_list[j]:
                    break;

                j = j + 1
                
            if j == len(target):
                return i

        return -1

if __name__ == "__main__":
    solution = Solution()
    if solution.longestCommonSubstring('ABCD', 'CBCE') == 2:
        print('test 1 pass')

    if solution.longestCommonSubstring('www.lintcode.com code', 'www.ninechapter.com code') == 9:
        print('test 2 pass')

    if solution.longestCommonSubstring('abc', 'a') == 1:
        print('test 3 pass')