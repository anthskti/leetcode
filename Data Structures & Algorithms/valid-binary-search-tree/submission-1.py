# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # output is a boolean whether root is valid bst or not
        # we validate the left branch first by checking if the parent node is more then the left child. 
        #then we do the same to the right, but right child is larger than parent. 
        def dfs(node, left, right):
            if not node:
                return True
            
            if (left < node.val and node.val < right ):
                return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            else:
                return False
        return dfs(root, float('-inf'), float('inf'))

        # Space O(h), recursion, height of the tree
        # Time O(n), how many elements

        