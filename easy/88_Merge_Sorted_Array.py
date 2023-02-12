class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) > m:
            for i in range(n):
                nums1.pop()
        merge_num = []
        while nums1:
            merge_num.append(nums1.pop())
        while nums2:
            merge_num.append(nums2.pop())
        merge_num.sort()
        while merge_num:
            nums1.append(merge_num.pop(0))