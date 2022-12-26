class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,num in enumerate(nums):
            j = target - num
            if j not in h:
                h[num] = i
            else:
                return [h[j],i]
            