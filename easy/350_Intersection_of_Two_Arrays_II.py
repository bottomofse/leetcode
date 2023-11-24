class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dic = {}
        for i in nums1:
            if i in nums1_dic:
                nums1_dic[i] += 1
            else:
                nums1_dic[i] = 1
        ret_list = []
        for i in nums2:
            if i in nums1_dic and nums1_dic[i] >= 1:
                nums1_dic[i] -= 1
                ret_list.append(i)
        return ret_list
