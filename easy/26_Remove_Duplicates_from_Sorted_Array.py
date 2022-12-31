class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        NonDuplicatedList = []
        while nums:
            tmp = nums.pop(0)
            if len(NonDuplicatedList) == 0:
                NonDuplicatedList.append(tmp)
            elif NonDuplicatedList[-1] != tmp:
                NonDuplicatedList.append(tmp)
        while NonDuplicatedList:
            tmp = NonDuplicatedList.pop(0)
            nums.append(tmp)
        return len(nums)
