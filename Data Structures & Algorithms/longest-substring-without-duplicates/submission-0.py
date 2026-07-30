class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Door method.
        n = len(s)
        charSet = set() 
        res = 0
        # left pointer
        l = 0
        # right pointer
        for r in range(n):
            # removes duplicate
            while s[r] in charSet: # purpose is to keep it non-duplicate
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l + 1) # checks the difference of the substring, sees which is bigger

        return res