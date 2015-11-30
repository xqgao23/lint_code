#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def anagram(self, s, t):
        if len(s) != len(t):
            return False

        l1 = list(s)
        l2 = list(t)

        l1.sort()
        l2.sort()

        for index in range(len(l1)):
            if l1[index] != l2[index]:
                return False

        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.anagram('django', 'naogdj'))