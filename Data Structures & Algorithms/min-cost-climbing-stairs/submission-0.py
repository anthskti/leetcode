class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # subproblem: at this step, what is the lowest cost
        # recurrence: dp[i] = cost[i]+min(dp[i−1],dp[i−2])

        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]

        # bottom up solution, using previous data, build up
        # top down solution, having a cache, and building up to the end of the staircasde using depths first search tree type thing.

