# Intuition
# Very similar to combination sum 2.
# Instead of adding, just append each potential value to the list
# If the nums[index] == value, skip it 
# have to implement for loop 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        

        def dfs(i):
            if len(subset) >= len(nums):
                res.append(subset.copy())
                return
            for j in range(len(nums)):
                if nums[j] in subset:
                    continue
                subset.append(nums[j])
                dfs(j+1)
                subset.pop()

        dfs(0)

        return res
        