# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we're solving for a boolean, checking fit het ree is balanced via their height
        # there is some formula.
        # O(n) elements time

        # how we can approach this problem is starting at the root. 
        # (it might be a recursive solution)
        # at each node, we can check left and right.
        # however we can only look at iterations of 1

        # my intuitive solution is at the root, check it's children if its equal to its val + 1 or val + 2. however this fails during deeper runs ex example2.

        # my second solution is to build the tree and compare, but that's also expensive approach as it's O(nlogn) (if not sorted) + O(n) comparison, ultimately O(n) space which isn't ideal.

        # okay, so I'm lowkey stuck. what should i do? look at previous questions solutions to warm me up.

        # okay, we can use a stack data structure to traverse

        # how would depth first search work on this?
        # we can keep a set of elements, but that won't configure into anything


        # I think i misunderstood the question
        # goal: return a binary tree that's height is balanced at every parent node. 
        # we can use DFS to review each parent node and compare their heights if it validates the condition. if it fails, since all values.        

        def dfs(node):
            if not root:
                return 0
            
            if node.left: 
                left = dfs(node.left)
            else:
                left = 0

            if node.right:    
                right = dfs(node.right)
            else:
                right = 0
            
            # this is the case if any of the subtrees failed the condition
            if abs(left - right) > 1 or left < 0 or right < 0:
                return -1
            
            return 1 + max(left, right)


        res = dfs(root)
        if res == -1:
            return False
        
        return True


        
        