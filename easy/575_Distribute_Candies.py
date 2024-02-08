class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        check = {}
        for i in candyType:
            check[i] = 0
        return min(len(candyType) // 2, len(check))