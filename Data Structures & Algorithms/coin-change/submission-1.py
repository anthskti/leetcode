class Solution:
    def coinChange(self, coins: List[int], C: int) -> int:
        dp = [C + 1] * (C + 1) 
        dp[0] = 0

        for value in range (1, C + 1):
            for coin in coins:
                if (value - coin >= 0):
                    dp[value] = min(dp[value], 1+dp[value - coin])
        if dp[C] != C+1:
            return dp[C]
        else:
            return -1 
	
