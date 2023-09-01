class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        maximum = -1
        minimum = 1000000
        if len(prices) == 1:
            return 0
        for i in range(len(prices)):
            maximum = prices[i]
            if prices[i] < minimum:
                minimum = prices[i]
            if maximum - minimum > result:
                result = maximum - minimum    
        return result
