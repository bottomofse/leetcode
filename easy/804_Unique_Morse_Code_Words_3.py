class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        check = set()
        for i in words:
            morse = ''
            for j in i:
                morse += table[(ord(j) - 97)]
            check.add(morse)
        return len(check)

        