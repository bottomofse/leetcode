class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        kakunin = [0 for i in range(len(nums) + 1)]
        kakunin[0] = 1
        for i in nums:
            kakunin[i] = 1
        ret = []
        for idx, num in enumerate(kakunin):
            if num == 0:
                ret.append(idx)
        return ret
