# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return the k'th smallest element integer
        # we can utilize the depths first search property
        # growing towards the next value
        count = k
        ans = root.val

        def dfs(node):
            nonlocal count, ans
            if not node:
                return 

            left_res = dfs(node.left)
            if count == 0:
                return 
            count -= 1
            if count == 0:
                ans = node.val
                return 
            
            dfs(node.right)

        dfs(root)

        return ans

    # Time O(n)
    # Space O(n)