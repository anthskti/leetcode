# Operation	Time
# insert	O(L)
# search	O(L)
# startsWith	O(L)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for l in word: # For each letter
            i = ord(l) - ord("a") # unicode
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word: 
            i = ord(l) - ord("a") 
            if curr.children[i] == None:
                return False # no more letters match
            curr = curr.children[i]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for l in prefix: 
            i = ord(l) - ord("a") 
            if curr.children[i] == None:
                return False # no more letters match
            curr = curr.children[i]
        return True
        
        