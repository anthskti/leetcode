"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Intuition
        # Hashmap, adding all the values

        # initalizing the hashmap
        copyMap = collections.defaultdict(lambda:Node(0))
        copyMap[None] = None

        cur = head
        while cur:
            copyMap[cur].val = cur.val
            copyMap[cur].next = copyMap[cur.next]
            copyMap[cur].random = copyMap[cur.random]
            cur = cur.next

        return copyMap[head]
            