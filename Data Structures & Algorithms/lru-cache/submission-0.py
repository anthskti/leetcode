class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # 1 class, 2 functions
    # class defines some structure for LRUCache
    # init is with capacity (first example is 2)
    # get -> returns a key, -1 if doesn't exist
    # put -> returns nothing, updates the value of the key or adds in cache

    # To get O(1) time for get and put, the best data structure is hashmap

    # in order to keep track of the most recently used -> least recently used
    # we can use pointers; but that'd only work for two positions; for more we can use a linkedlist (doubly for reordering them)

    

    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key's to nodes
        
        self.left = Node(0,0)
        self.right = Node(0,0)

        # left -> right == least recent -> most recent
        self.left.next = self.right
        self.right.prev = self.left
    
    # remove from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        # remove node
        prev.next = nxt
        nxt.prev = prev

    # insert at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        
        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove -> reinsert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            # remove the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        
