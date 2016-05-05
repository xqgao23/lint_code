#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    """
    @param source : source string
    @param target : target string
    @return :  return the first index of source string contain target string, if does not exist, return -1
    """
    def strStr(self, source, target):
        if source == None or target == None:
            return -1

        if len(source) < len(target):
            return -1

        if len(target) == 0:
            return 0

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
        

    def new_index_get(self, t_list):
        if len(t_list) == 1:
            return -1

        j_len = len(t_list) - 1
        while j_len >= 0:
            found = True

            for i in range(j_len):
                if t_list[i] != t_list[len(t_list) - j_len + i]:
                    found = False
                    break
            if found:
                return j_len - 1

            j_len = j_len - 1
        return -1

    def strStr_kmp(self, source, target):
        if source == None or target == None:
            return -1

        if len(source) < len(target):
            return -1

        if len(target) == 0:
            return 0

        s_list = list(source)
        t_list = list(target)

        t_index = -1
        for s_index in range(len(s_list)):
            while t_index >= 0 and t_list[t_index + 1] != s_list[s_index]:
                t_index = self.new_index_get(t_list[:t_index + 1])

            if t_list[t_index + 1] == s_list[s_index]:
                t_index = t_index + 1

            if t_index == len(target) - 1:
                return s_index - len(target) + 1

        return -1

        

if __name__ == "__main__":
    solution = Solution()
    if solution.strStr('source', 'target') == solution.strStr_kmp('source', 'target'):
        print('test 1 pass')

    if solution.strStr('abcdbcabcdefg', 'bcdbcd') == solution.strStr_kmp('abcdbcabcdefg', 'bcdbcd'):
        print('test 2 pass')

    if solution.strStr('abababaababacb', 'ababacb') == solution.strStr_kmp('abababaababacb', 'ababacb'):
        print('test 3 pass')
