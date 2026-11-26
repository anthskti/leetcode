class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return an array of the arrays products except itself.
        # Desires O(n) time
        
        # since 0 exist, my original intuition fails
        # bitwise?

        # using prefix and suffix, flagging it by 1 indice
        # we're basically creating a list of all the left and right side 
        # then multiply it together

        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i - 1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res

        # Time O(n)
        # Space O(n)
