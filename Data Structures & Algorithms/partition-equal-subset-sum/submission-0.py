class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum(nums) % 2, that means it can be divided in two
        # sum(nums)// 2 is our goal for each subset. 
        # have two choices, picking some nums[i][j] or 0

        # Subproblem: can we find a sum a subset of [0...j] that sums to i
        # Recurrence: dp[i] = dp[i] or dp[i−nums[j]]
        # Initalization: 

        if sum(nums) % 2 == 1:
            return False
        n = len(nums)
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(n - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)

            dp = nextDP
 
        if target in dp:
            return True
        else:
            return False