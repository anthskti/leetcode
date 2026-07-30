class Solution:
    def rob(self, nums: List[int]) -> int:
        # what is the maximum money you can earn at house i?
        # max(dp[i], dp[i-1])
        # dp[0] = nums[0]
        n = len(nums)
        dp = [0] * n 
        dp[0] = nums[0]
        if n == 1:
            return dp[0]
        if n == 2:
            return max(nums[0], nums[1])
        # o(n^2)
        # for i in range(n):
        #     for j in range(i-1):
        #         dp[i] = max(dp[i], dp[j] + nums[i])

        for i in range(n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]