class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [0] *(n)
        pos = 0

        for i in range (1, n):
            if(prices[pos] > prices[i]):
                pos = i
            elif(prices[i] - prices[pos] >= 0):
                dp[i] = prices[i] - prices[pos]

        return max(dp)