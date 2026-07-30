class Solution {
    public int climbStairs(int n) {
        // O(n) time complexity
        // O(n) space

        // Memoization Solution uses recursion
        // Base case
        if (n <= 2) return n;

        // Bottom Up Appoarch
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i-1]+dp[i-2];
        } 
        return dp[n];
    }
}
