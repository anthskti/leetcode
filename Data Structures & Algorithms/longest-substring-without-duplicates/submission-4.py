class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return the length of the substring without repeating chars
        # sliding window as we need to keep area
        # left and right pointer, if there doesn't exist a duplicate, move right
        # if there does, move left
        
        max_count = 0
        rep = set()
        l = 0

        for r in range(len(s)):
            if s[r] in rep:
                while s[r] in rep:
                    rep.remove(s[l])
                    l += 1

            rep.add(s[r])
            max_count = max(r - l + 1, max_count)
                
        
        return max_count

        # Time O(n)
        # Space O(n)

        # count and r - l + 1 do the same thing, but maintain less states.
            
            
            
            
             
            




        