#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string what present as binary, 'ERROR' if cannot present in 32 chars.
    def binaryRepresentation(self, n):  
        num = n.split('.')
        ddec = self.ddec2bin(float('0.' + num[1]))
        dec = self.dec2bin(int(num[0]))

        if len(ddec) >= 32:
            return 'ERROR'

        if len(ddec) > 0:
            return '.'.join([dec, ddec])
        elif len(dec):
            return dec


    def ddec2bin(self, d):
        n = d
        c = []
        while n != 0:
            n = n * 2
            if n >= 1:
                n = n - 1
                c.append('1')
            else:
                c.append('0')

            if len(c) > 32:
                break
        return ''.join(c)


    def dec2bin(self, d):
        if d == 0:
            return '0'
            
        n = d
        c = []
        while n != 0:
            c.insert(0, str(n & 0x1))
            n = n >> 1
        return ''.join(c)


if __name__ == '__main__':
    solution = Solution()
    if solution.binaryRepresentation('3.72') == "ERROR":
        print('test 1 pass')
    if solution.binaryRepresentation('3.5') == '11.1':
        print('test 2 pass')
