# Intuition
# Backtracking. since we are look at EVERY POSSIBLE SUBSET, this looks like a BFS approach
# Going to go as
# 
# Brute Force approach: for each value, incrementally add their higher subset values, if its in, then go next.      

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize nested list 
        res = []
        subset = []
        
        # res.append([])

        def dfs(i): 
            if i >= len(nums):
                res.append(subset.copy()) # Deep copy
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)


        dfs(0)
        return res
