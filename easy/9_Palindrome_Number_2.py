class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = ''
        for i in str(x):
            rev = i + rev
        if str(x) == rev:
            return True
        return False
