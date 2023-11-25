from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        ret = []
        for i in nums2:
            t = c.get(i)
            if t is not None and t > 0:
                c[i] -= 1
                ret.append(i)
        return ret
