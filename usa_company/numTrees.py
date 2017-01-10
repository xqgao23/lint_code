#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    # @param n: An integer
    # @return: An integer
    def numTrees(self, n):
        numArray = [x + 1 for x in range(n)]
        self.max_trees = {}
        return self.get_max_trees(numArray)
        
    def get_max_trees(self, numArray):
        if len(numArray) < 3:
            if len(numArray) == 0:
                return 1
            else:
                return len(numArray)
        
        array_str = str(numArray)
        if array_str in self.max_trees:
            return self.max_trees[array_str]

        total_counts = 0
        for i in range(len(numArray)):
            left_counts = self.get_max_trees(numArray[:i])
            right_counts = self.get_max_trees(numArray[i + 1:])
            
            total_counts = left_counts * right_counts + total_counts
        self.max_trees[array_str] = total_counts
        return total_counts

if __name__ == '__main__':
    solution = Solution()
    if solution.numTrees(0) == 1:
        print('test 1 pass')
    if solution.numTrees(15) == 9694845:
        print('test 2 pass')