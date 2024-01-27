class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if self.isAllCapitals(word):
            return True
        if self.isAllNotCapitals(word):
            return True
        if self.isOnlyFirstCapital(word):
            return True
        return False

    def isAllCapitals(self, word: str) -> bool:
        for i in word:
            if not i.isupper():
                return False
        return True
            
    def isAllNotCapitals(self, word: str) -> bool:
        for i in word:
            if i.isupper():
                return False
        return True
        
    def isOnlyFirstCapital(self, word: str) -> bool:
        if not word[0].isupper:
            return False
        for i in range(1, len(word)):
            if not word[i].islower():
                return False
        return True