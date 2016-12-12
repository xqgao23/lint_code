#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    # @param n an integer
    # @return a integer with n! trailing zeros

    def trailingZeros(self, n):
        if n <= 1:
            return 0
        
        power = 5
        zero_counts = 0
        while (int(n / power) > 0):
            zero_counts = zero_counts + int(n / power)
            power = power * 5

        return zero_counts

if __name__ == '__main__':
    soltion = Solution()
    if soltion.trailingZeros(11) == 2:
        print('test 1 pass!')
    
    if soltion.trailingZeros(20) == 4:
        print('test 2 pass!')

    if soltion.trailingZeros(50) == 12:
        print('test 3 pass!')