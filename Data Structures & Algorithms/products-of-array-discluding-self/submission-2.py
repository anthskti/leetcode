class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intuition: brute force O(n^2), for each value, loop through each but ignore current.
        
        # res = []
        # for i in range(len(nums)):
        #     temp = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             temp *= nums[j]
            
        #     res.append(temp)

        # return res

        # intuition for O(2n), pre + post fix
        # set output to prefixes, then do another loop for post fixes

        res = [1] * (len(nums))

        prefix = 1
        for i in range (len(nums)):
            res[i] *= prefix 
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]


        return res
            