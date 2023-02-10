class Solution:
    def climbStairs(self, n: int) -> int:
        step_cnt_list = [0 for i in range(n + 1)]
        step_cnt_list[0] = 1
        for i in range(1, n + 1):
            if i - 2 >= 0:
                step_cnt_list[i] += step_cnt_list[i - 2]
            if i - 1 >= 0:
                step_cnt_list[i] += step_cnt_list[i - 1]
        return step_cnt_list[-1]
