class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = 0
        tmp = num
        while tmp:
            bitmask = bitmask << 1
            bitmask += 1
            tmp = tmp // 2
        return (~num) & bitmask
