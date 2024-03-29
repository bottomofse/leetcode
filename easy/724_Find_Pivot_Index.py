class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(0, len(nums)):
            if i > 0:
                left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        return -1