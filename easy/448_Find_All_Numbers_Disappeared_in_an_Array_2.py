class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {i:True for i in nums}
        ret = []
        for i in range(1, len(nums) + 1):
            if i not in dic:
                ret.append(i)
        return ret
