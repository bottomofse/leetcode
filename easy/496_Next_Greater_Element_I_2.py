class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        dic_nums2 = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if not stack:
                dic_nums2[nums2[i]] = -1
            else:
                dic_nums2[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        ret = []
        for i in nums1:
            ret.append(dic_nums2[i])
        return ret
