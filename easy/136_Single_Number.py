class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check_dic = {}
        for i in nums:
            if i in check_dic:
                del check_dic[i]
            else:
                check_dic[i] = 0
        for i in check_dic:
            return i