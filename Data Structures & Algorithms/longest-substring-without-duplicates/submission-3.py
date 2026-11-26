class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return the length of the substring without repeating chars
        # sliding window as we need to keep area
        # left and right pointer, if there doesn't exist a duplicate, move right
        # if there does, move left
        
        max_count = 0
        count = 0
        rep = set()
        l = 0

        for r in range(len(s)):
            if s[r] in rep:
                while s[r] in rep:
                    rep.remove(s[l])
                    l += 1
                    count -= 1

            rep.add(s[r])
            count += 1
            max_count = max(count, max_count)
                
        
        return max_count

        # Time O(n)
        # Space O(n)
            
            
            
            
             
            




        