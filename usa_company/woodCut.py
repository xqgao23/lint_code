#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param L: Given n pieces of wood with length [i]
    @param k: An integer
    @return : The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if L == None:
            return 0

        longest_wood = self.get_longest_wood(L)
        
        max_length = longest_wood
        min_length = 1
        target_length = min_length
        max_length_of_pieces = 0
        while max_length >= min_length:
            target_length = int((max_length + min_length) / 2)
            pieces_of_woods = self.get_pieces_of_woods(L, target_length)
            if pieces_of_woods >= k:
                if max_length_of_pieces < target_length:
                    max_length_of_pieces = target_length
                    min_length = target_length + 1
                else:
                    break
            else:
                max_length = target_length - 1

        return max_length_of_pieces



    def get_pieces_of_woods(self, L, wood_length):
        pieces = 0
        
        for l in L :
            pieces = pieces + int(l / wood_length)

        return pieces

    def get_longest_wood(self, L):
        max_length = 0
        for l in L:
            if l > max_length:
                max_length = l
        return max_length


if __name__ == "__main__":
    solution = Solution()
    if solution.woodCut([232, 124, 456], 7) == 114:
        print('test 1 pass')
    