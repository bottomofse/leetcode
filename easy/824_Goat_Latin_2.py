class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split(' ')
        vowel = set('aiueoAIUEO')
        for i, val in enumerate(s):
            s[i] = val if val[0] in vowel else val[1:] + val[0]
            s[i] += 'ma' + 'a' * (i + 1)
        return ' '.join(s)