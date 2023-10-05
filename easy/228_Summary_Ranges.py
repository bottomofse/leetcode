class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arrow = '->'
        queue = []
        result = []
        for i in nums:
            if not queue:
                queue.append(i)
                continue
            if queue[-1] + 1 == i:
                queue.append(i)
                continue
            else:
                if queue[0] == queue[-1]:
                    result.append(str(queue[0]))
                else:
                    result.append(str(queue[0]) + arrow + str(queue[-1]))
                queue = []
                queue.append(i)
        if queue:
            if queue[0] == queue[-1]:
                result.append(str(queue[0]))
            else:
                result.append(str(queue[0]) + arrow + str(queue[-1]))
        return result
