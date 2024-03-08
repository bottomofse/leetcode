class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost) + 1)]
        for idx, val in enumerate(dp):
            if idx == 0 or idx == 1:
                dp[idx] = 0
                continue
            dp[idx] = min(dp[idx- 1] + cost[idx - 1], dp[idx- 2] + cost[idx - 2])
        return dp[-1]