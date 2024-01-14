class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        before = -1
        max_num = 0
        cur_consecutive = 0
        for i in nums:
            if i == 0:
                cur_consecutive = 0
            else:
                cur_consecutive += 1
                max_num = max(cur_consecutive, max_num)
        return max_num