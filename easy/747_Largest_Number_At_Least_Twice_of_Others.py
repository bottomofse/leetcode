class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        top = nums[0]
        second = -1
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] > top:
                second = top
                top = nums[i]
                idx = i
                continue
            if nums[i] > second:
                second = nums[i]
                continue
        return idx if top >= second * 2 else -1
    