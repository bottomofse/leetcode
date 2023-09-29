class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = {}
        for i in nums:
            if i in duplicate_check:
                return True
            else:
                duplicate_check[i] = 0
        return False
