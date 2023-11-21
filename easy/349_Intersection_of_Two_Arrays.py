class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret_list_dic = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ret_list_dic[nums1[i]] = 1
        ret_list = []
        for i in ret_list_dic:
            ret_list.append(i)
        return ret_list
