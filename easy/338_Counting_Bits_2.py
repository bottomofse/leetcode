class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        result = [0, 1]
        cur_two = 4
        index = 0
        for i in range(2, n + 1):
            if i >= cur_two:
                index = 0
                cur_two *= 2
            result.append(result[index] + 1)
            index += 1
        return result
