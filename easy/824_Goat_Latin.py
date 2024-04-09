class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split(' ')
        vowel = set(['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O', ])
        for i, val in enumerate(s):
            if val[0] in vowel:
                s[i] = val + 'ma' + 'a' * (i + 1)
            else:
                s[i] = val[1:] + val[0] + 'ma' + 'a' * (i + 1)
        return ' '.join(s)