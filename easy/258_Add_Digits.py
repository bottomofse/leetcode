class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            tmp = 0
            for i in num_str:
                tmp += int(i)
            num_str = str(tmp)
        return int(num_str)
