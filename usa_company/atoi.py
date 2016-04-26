#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param str : a string
    @return : an integer
    """
    char2int = { '0' : 0, '1': 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9 }

    def atoi(self, str):
        if str == None or len(str) == 0:
            return 0

        signed = False
        point = False
        base = 0
        start_count = False
        value = 0.0

        for i in range(len(str)):
            if not start_count:
                if str[i] == '-':
                    signed = True
                    start_count = True
                    continue
                elif str[i] == '+':
                    signed = False
                    start_count = True
                    continue
                elif str[i] == ' ':
                    continue   
                elif not str[i] in self.char2int.keys():
                    break
                else:
                    start_count = True

            if not point:
                if str[i] == '.':
                    point = True
                    continue
            
            if not str[i] in self.char2int.keys():
                break

            value = value * 10 + self.char2int[str[i]]
            if point:
                base = base + 1

        if base > 0:
            value = value / pow(10, base)

        value = -value if signed else value
        if value > 2147483647:
            value = 2147483647
        if value < -2147483648:
            value = -2147483648

        if value == int(value):
            value = int(value)
        return value
        

if __name__ == "__main__":
    solution = Solution()
    if solution.atoi('    52lintcode   ') == 52:
        print('test -3 pass ')

    if solution.atoi('    -5211314') ==  -5211314:
        print('test -2 pass')

    if solution.atoi('1.0') == 1:
        print('test -1 pass')

    if solution.atoi('-100.23') == -100.23:
        print('test 0 pass')

    if solution.atoi('-132335.25807') == -132335.25807:
        print('test 1 pass')

    if solution.atoi('+23840280.934792') == 23840280.934792:
        print('test 2 pass')

    if solution.atoi('023849279') == 23849279:
        print('test 3 pass')

    if solution.atoi('830804sjdkj-9792348dsfs') == 0:
        print('test 4 pass')

    if solution.atoi('9237482794792794729374923749327984798327947294345309503953') == 2147483647:
        print('test 5 pass')

    if solution.atoi('2147483647') == 2147483647:
        print('test 6 pass')

    if solution.atoi('2147483648') == 2147483647:
        print('test 7 pass')

    if solution.atoi('-2342804802830480283049820') == -2147483648:
        print('test 8 pass')

    if solution.atoi('-2147483648') == -2147483648:
        print('test 9 pass')

    if solution.atoi('-2147483649') == -2147483648:
        print('test 10 pass')

    if solution.atoi('0.0') == 0:
        print('test 11 pass')

    if solution.atoi('-0.37979') == -0.37979:
        print('test 12 pass')