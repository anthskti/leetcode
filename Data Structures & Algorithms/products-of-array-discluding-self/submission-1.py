class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intuition: O(n^2), for each value, loop through each but ignore current.
        
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i != j:
                    temp *= nums[j]
            
            res.append(temp)

        return res