class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right + 1):
            origin = i
            n = origin
            flg = True
            while n > 0:
                if n % 10 == 0 or origin % (n % 10) != 0:
                    flg = False
                    break
                n = n // 10
            if flg:
                ret.append(i)
        return ret
            
            
                    
            