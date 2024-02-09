class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_length = 0
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if i + 1 in dic:
                max_length = max(max_length, dic[i] + dic[i + 1])
            if i - 1 in dic:
                max_length = max(max_length, dic[i] + dic[i - 1])
        return max_length