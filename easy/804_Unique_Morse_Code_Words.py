class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        morse = {}
        for i in range(26):
            morse[alphabet[i]] = table[i]
        check = {}
        for i in words:
            to_morse = ''
            for j in i:
                to_morse += morse[j]
            check[to_morse] = True
        return len(check)
