#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param n: svn num
    @return : return the first bad version
    """
    def findFirstBadVersion(self, n):
        max_index = n
        min_index = 1
        bad_index = n

        while max_index >= min_index:
            mid_index = int((max_index + min_index) / 2)
            if SVNRepo.isBadVersion(mid_index):
                bad_index = mid_index
                max_index = mid_index - 1
            else:
                min_index = mid_index + 1

        return bad_index


class SVNRepo:
    @classmethod
    def isBadVersion(cls, id):
        if id >= 1000:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    if solution.findFirstBadVersion(10000) == 1000:
        print('test 1 pass')