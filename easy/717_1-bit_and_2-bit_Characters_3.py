class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        ret = True
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                ret = True
                continue
            if bits[i] == 1:
                i += 2
                ret = False
                continue
        return ret