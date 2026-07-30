class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCounter = Counter(s)
        tCounter = Counter(t)

        for i in sCounter:
            if sCounter.get(i) != tCounter.get(i):
                return False

        return True
        