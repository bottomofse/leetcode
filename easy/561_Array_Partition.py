class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        cnt = 0
        result = 0
        for i in sorted_list:
            if cnt == 0:
                result += i
                cnt = 1
            else:
                cnt = 0
        return result