# Intuition
# Backtracking. since we are look at EVERY POSSIBLE SUBSET, this looks like a BFS approach
# Going to go as running DFS from index 0. O(V+E)
# Need to run two BFS since we have to include current point and exclude current point. thats why its 2^n
#                        []
#              ┌──────────┴──────────┐
#         include 1             exclude 1
#              ↓                     ↓
#             [1]                   []
#        ┌─────┴─────┐         ┌─────┴─────┐
#   include 2   exclude 2  include 2   exclude 2
#        ↓           ↓         ↓           ↓
#      [1,2]        [1]       [2]         []
#     ┌──┴──┐     ┌──┴──┐   ┌──┴──┐     ┌──┴──┐
#    +3   skip   +3   skip +3   skip   +3   skip
#     ↓     ↓     ↓     ↓   ↓     ↓     ↓     ↓
# [1,2,3] [1,2] [1,3]  [1] [2,3] [2]   [3]   []
    

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
