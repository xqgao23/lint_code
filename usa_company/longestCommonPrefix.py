#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : A string
    @param B : B string
    @return :  return the max common string in A and B string
    """
    def longestCommonPrefix(self, strs):
        if strs == None or len(strs) <= 1:
            return 0

        str = strs[0]
        left_strs = strs[1:]

        for i in range(len(str)):
            for test_str in left_strs:
                if len(test_str) <= i:
                    return str[:i]
                
                if test_str[i] != str[i]:
                    return str[:i]

        return str


if __name__ == "__main__":
    solution = Solution()
    if solution.longestCommonPrefix([ 'A', "ABCD", "ABEF", "ACEF", "A"]) == 'A':
        print("test 1 pass")

    if solution.longestCommonPrefix([ "ABCDEFG", "ABCEFG", "ABCEFA"]) == "ABC":
        print("test 2 pass")
