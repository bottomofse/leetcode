class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            if not isBadVersion(middle) and isBadVersion(middle + 1):
                return middle + 1
            if not isBadVersion(middle) and not isBadVersion(middle + 1):
                left = middle
                continue
            if isBadVersion(middle) and isBadVersion(middle + 1):
                right = middle
                continue
