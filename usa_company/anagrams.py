#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def anagrams(self, strs):
        # write your code here
        str_len = len(strs)
        if str_len < 2:
            return []
        anagrams_str = []
        key_map = {}

        for s in strs:
            key = self.str_to_key(s)
            if key in key_map:
                anagrams_str.append(s)
                if not key_map[key] in anagrams_str:
                    anagrams_str.append(key_map[key])
            else:
                key_map[key] = s

        return anagrams_str

    def str_to_key(self, s):
        c_count = [0] * 26
        for c in list(s):
            i = ord(c) - ord('a')
            c_count[i] = c_count[i] + 1
        return tuple(c_count)

if __name__ == "__main__":
    solution = Solution()
    if solution.anagram(["lint","intl","inlt","code"] == ["lint","inlt","intl"]:
        print('pass')
