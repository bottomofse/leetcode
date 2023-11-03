class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        not_zero = []
        while nums:
            tmp = nums.pop()
            if tmp == 0:
                zeroes.append(tmp)
            else:
                not_zero.append(tmp)
        while not_zero:
            nums.append(not_zero.pop())
        while zeroes:
            nums.append(zeroes.pop())
