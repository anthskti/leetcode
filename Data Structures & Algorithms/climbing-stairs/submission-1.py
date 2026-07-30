class Solution:
    def climbStairs(self, n: int) -> int:
        # subproblem: how many stairs can we get up in n-1 step?
        # recurrence: Step(n-2) + Step(n-1)

        if (n<= 2):
            return n

        # initalize an array full of zeroes
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]