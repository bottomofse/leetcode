import copy
from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_idx = deque()
        aiueo = 'aiueoAIUEO'
        for i in range(len(s)):
            if s[i] in aiueo:
                vowels_idx.append(i)
        ret_str = list(copy.copy(s))
        while len(vowels_idx) > 1:
            forward ,back = vowels_idx.popleft(), vowels_idx.pop()
            ret_str[forward], ret_str[back] = ret_str[back], ret_str[forward]
        return ''.join(ret_str)
