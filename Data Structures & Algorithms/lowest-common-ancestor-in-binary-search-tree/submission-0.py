# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # We're supposed to output the TreeNode of the values lowest common anscestor
        # we could utilize a BFS or DFS here
        # why? because since its a balance tree w unique values
        # idk
        # I think we scale up the tree a
        # we can start at the root and utilize DFS to see if its on the branch. 

        # using the balance nature of trees, we can compare values to the root the find out which side they're on.

        # in my head there are three cases. 

        curr = root
        
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr

            

            
        

