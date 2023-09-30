class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k_dict = {}
        for i, v in enumerate(nums):
            j = k_dict.get(v, -1)
            if j != -1 and abs(i - j) <= k:
                return True
            else:
                k_dict[v] = i
        return False
