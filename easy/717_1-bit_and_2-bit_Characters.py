class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        while bits:
            a, b = -1,-1
            a = bits.pop(0)
            if a != 0 and bits:
                b = bits.pop(0)
        return b == -1