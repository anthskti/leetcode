# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the output should be a boolean, highlighting if the trees are exactly the same
        # the brute force way would to compare ???
        # we could use a bfs approach, since the stack output be the exact same? O(n) time complexity
        # i'm thinking we could use the stack to our advantange and compare values directly


        queue_p = []
        queue_p.append(p)

        queue_q = []
        queue_q.append(q)
        
        while queue_p and queue_q:
            a = queue_p.pop(0)
            b = queue_q.pop(0)
            # edge case: empty tree node
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            queue_p.append(a.left)
            queue_p.append(a.right)

            queue_q.append(b.left)
            queue_q.append(b.right)
        
        return True