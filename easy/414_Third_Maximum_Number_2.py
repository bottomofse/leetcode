class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t = sorted(list(set(nums)))
        if len(t) < 3:
            return t[-1]
        return t[-3]
