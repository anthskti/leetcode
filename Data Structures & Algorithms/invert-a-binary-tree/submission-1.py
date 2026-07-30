# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case
        if not root:
            return None

        stack = [root]

        while stack != []:
            node = stack.pop()
            # swap
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)

        return root 


        