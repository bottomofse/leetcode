class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count(n):
            cnt = 0
            while n:
                cnt += (n & 1)
                n >>= 1
            return cnt

        def get_h(n):
            return n >> 6

        def get_m(n):
            return n & 0b0000111111

        ret = []
        for i in range(1024):
            if count(i) == turnedOn:
                h = get_h(i)
                if h > 11: continue
                m = get_m(i)
                if m > 59: continue
                s = str(h) + ':' + ('0' + str(m))[-2:]
                ret.append(s)
        return ret
