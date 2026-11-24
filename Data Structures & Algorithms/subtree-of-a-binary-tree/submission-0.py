# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # our goal is to output a boolean value whether the subtree exists in the root folder. 
        # i think the best goal is to dfs compare. 
        # two problems:
        # 1. finding the subroot node
        # 2. comparing whether the trees are the same

        def dfs(p):
            if not p: 
                return False
            
            if p.val == subRoot.val:
                if isSameTree(p, subRoot):
                    return True

            return dfs(p.left) or dfs(p.right)
            

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
        

        return dfs(root)