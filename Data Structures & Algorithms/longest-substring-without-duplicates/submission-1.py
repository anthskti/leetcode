class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # output: an integer of the longest substring w/o repeating chars
        # an approach I can think of is a sliding window
        # O(n) time with O(n) space though
        # we move the right pointer, until we see a duplicate, where we'll once we do, we'll constantly move the left pointer -> right pointer until no dups.

        # set() could work in some cases, but not all
        count = 0

        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            count = max(count, r-l+1)
        
        return count
            




        