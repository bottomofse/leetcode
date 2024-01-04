class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_set = set([i for i in range(1, len(nums) + 1)])
        return list(all_set - set(nums))
