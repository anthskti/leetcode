# Intuition
# This feels like another DFS applied
# Run DFS, and if the number goes above the target, return
# Compared to "all subset" our DFS will input something else,
# Since we can infintely use the numbers. we should 

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total = 0

        def dfs(i, total):
            if i >= len(nums): # Checking elements
                return
            elif total > target: # Failure Case
                return
            elif total == target: # Target Case 
                res.append(subset.copy())
                return 
            else:
                subset.append(nums[i]) # add the i'th position 
                dfs(i, total + nums[i])
                subset.pop() # Skips i'th position and add.
                dfs(i+1, total)

            # this cycle will continue until all values are forced to "target"
            # so this could be pretty long


        dfs(0, total)

        return res