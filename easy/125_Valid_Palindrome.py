class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphabet_s = ''
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    only_alphabet_s += i.lower()
                else:
                    only_alphabet_s += i
        for i in range(len(only_alphabet_s)):
            forward = only_alphabet_s[i]
            back = only_alphabet_s[-(i + 1)]
            if forward != back:
                return False
        return True
