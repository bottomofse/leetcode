class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(list(jewels))
        cnt = 0
        for i in stones:
            if i in j:
                cnt += 1
        return cnt