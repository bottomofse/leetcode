import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dic = {}
        for i in nums:
            if i in count_dic:
                count_dic[i] += 1
            else:
                count_dic[i] = 1
        for i in count_dic:
            if count_dic[i] >= math.ceil(len(nums) / 2):
                return i