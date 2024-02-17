class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = {}
        dup = 0
        missing = 0
        for i in nums:
            if i in check:
                dup = i
            check[i] = 0
        for i in range(1, len(nums) + 1, 1):
            if i not in check:
                missing = i
                break
        return [dup, missing]