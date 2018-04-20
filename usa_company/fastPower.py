#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer what is (a ^ n) % b
    """
    def fastPower(self, a, b, n):
        if b == 0:
            return 0
        
        if n == 0:
            return 1 % b

        power = 1
        a = a % b
        while n > 0:
            if n % 2 == 1:
                power = (power * a) % b
            n = n / 2
            a = (a * a) % b
        return power

    def fastPower2(self, a, b, n):
        if b == 0:
            return 0

        if a == 1:
            return 1 % n

        self.npower = {}

        """
        a ^ n % b = (a % b) ^n % b
        """
        power_of_a = self.fPower2(a % b, n)
        
        return power_of_a % b

    def fPower2(self, a, n):
        if n == 0:
           return 1
        elif n == 1:
            return a

        power_base = [n]
        index = n
        while index > 1:
            index = int(index / 2)
            power_base.append(index)

        power = a
        index = len(power_base) - 1
        while index >= 0:
            if power_base[index] == 1:
                index -= 1
                continue

            if power_base[index] > 2 * power_base[index + 1]:
                power = power * power * a
            else:
                power = power * power
            index -= 1
        return power

   
    def fPower(self, a, n):
        if n == 0:
            return 1
        elif n == 1:
            return a

        if n in self.npower:
            return self.npower[n]
        
        if n % 2 == 0:
            self.npower[n] = self.fPower(a, int(n / 2)) * self.fPower(a, int(n / 2))
        else:
            self.npower[n] = self.fPower(a, int(n / 2)) * self.fPower(a, int(n / 2)) * a
            
        return self.npower[n]

if __name__ == "__main__":
    solution = Solution()
    if solution.fastPower(2, 3, 31) == 2:
        print('test 1 pass.')
    if solution.fastPower(1000, 1000, 1000) == 0:
        print('test 2 pass.')
    if solution.fastPower(0, 0, 2) == 0:
        print('test 3 pass')
    if solution.fastPower(1, 2147483647, 2147483647) == 1:
        print('test 4 pass')
    if solution.fastPower(2, 2147483647, 2147483647) == 2:
        print('test 5 pass')
    if solution.fastPower(31, 1, 0) == 0:
        print('test 6 pass ')
    