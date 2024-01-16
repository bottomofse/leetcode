class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums1)):
            num1existflg = False
            num1greaterflg = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    num1existflg = True
                if num1existflg and nums1[i] < nums2[j]:
                    ret.append(nums2[j])
                    num1greaterflg = True
                    break
            if not num1greaterflg:
                ret.append(-1)
        return ret
