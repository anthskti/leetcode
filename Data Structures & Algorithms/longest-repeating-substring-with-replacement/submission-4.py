class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return the int of the longest repeating substring

        # we can use a sliding window approach to find this substring

        #AAABABBBBB, ignore it and see the abstraction
        # we have just have to find the current largest string
        # and replace two valid replacements

        count = {}
        max_count = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1  

            max_count = max(max_count, r-l+1)  

        return max_count

        # Time O(n)
        # Space O(n)