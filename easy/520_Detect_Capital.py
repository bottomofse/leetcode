class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        FirstCapital = word[0].isupper()
        if len(word) >= 2 and FirstCapital and word[1].islower():
            FirstCapital = False
        for i in range(1, len(word)):
            if FirstCapital != word[i].isupper():
                return False
        return True