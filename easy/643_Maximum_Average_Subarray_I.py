from collections import deque
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = -99999999999
        q = deque()
        cur = 0
        for idx, val in enumerate(nums):
            cur += val
            q.append(val)
            if len(q) == k:
                maximum = max(maximum, cur / k)
                cur -= q.popleft()
        return maximum