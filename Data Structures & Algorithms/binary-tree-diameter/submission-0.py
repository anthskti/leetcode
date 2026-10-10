# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We have to output the diameter of the tree, aka the depth.
        # we can solve this using a depth first search (DFS) approach

        maximum = 0 
        # Always has 1 node in the tree
        
        def dfs(root):
            nonlocal maximum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maximum = max(maximum, left + right)

            return 1 + max(left, right)

        dfs(root)
        return maximum
        