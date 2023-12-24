class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = - (2 ** 32)
        second =  - (2 ** 32)
        third =  - (2 ** 32)
        cnt = 0
        for i in nums:
            if i > first:
                third = second
                second = first
                first = i
                cnt += 1
                continue
            if i == first:
                continue
            if i > second:
                third = second
                second = i
                cnt += 1
                continue
            if i == second:
                continue
            if i > third:
                third = i
                cnt += 1
                continue
        return third if cnt >= 3 else first
