class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        first = {}
        last = {}
        maximum_freq = 0
        for i,val in enumerate(nums):
            if val in freq:
                freq[val] += 1
                maximum_freq = max(maximum_freq, freq[val])
            else:
                freq[val] = 1
                maximum_freq = max(maximum_freq, freq[val])
            if val not in first:
                first[val] = i
            last[val] = i
        minimum = float('inf')
        for i in nums:
            if freq[i] == maximum_freq:
               minimum = min(minimum, last[i] - first[i] + 1)
        return minimum