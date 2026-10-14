"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we have to output a deep copy fo the list
        # what we can do, is since it is a adjacency list, we can use dfs on each node; when all nodes are visit, we make a node and append its values.

        # or for each node, we make a new one, and then dfs?
        # my question is how do we reconnect them again?

        # so we are dfs'ing; at each stage, we check if it exists. if it does, we return the list. else add it on our hashmap. in order to copy its neighbors, we check all current neighbors -> run dfs on those; since our base case holds, it'll append.
        if not node:
            return node
        
        clone = {}

        def dfs(n):
            if n in clone:
                return clone[n]

            copy = Node(n.val)
            clone[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
                

        # Time complexity O(n) which is O(V+E)
        