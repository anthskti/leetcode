# Intuition
# This is combination sum 1, but highlighting no duplicates. 
# I could do DFS again but instead I force the next value like I did in subsets
# Do I need to sort the candidates?
## I don't think I need to. since I'm brute force checking every value. 



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total = 0 
        candidates.sort()
        

        def dfs(i, total):
            if total == target: # Is target
                res.append(subset.copy())
                return 
            elif total > target: 
                return
            else:
                for j in range(i, len(candidates)):
                    if j > i and candidates[j] == candidates[j-1]:
                        continue

                    subset.append(candidates[j])
                    dfs(j+1, total + candidates[j])
                    subset.pop()
                    # dfs(j+1, total)


        dfs(0, total)
        return res 