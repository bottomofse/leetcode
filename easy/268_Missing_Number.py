class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums) + 1):
            dic[i] = 0
        for i in nums:
            dic.pop(i)
        for i in dic:
            return i
