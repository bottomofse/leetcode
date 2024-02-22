class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        before = -float('inf')
        cnt = 0
        max_cnt = 0
        for i in nums:
            if i > before:
                cnt += 1
                before = i
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
                before = i
        return max_cnt