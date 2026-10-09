class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # this problem outputs a length of a string
        # we're replacing k indexes, trying to maximize the longest substring 

        # I didn't read longest substring originally, was thinking of hashmapping and then + K < len() which would be a quick solution

        # With substring, we can look at a sliding door method
        # Our time complexity likely should be O(n); since brute force is O(n^2)

        # ascii A = 65
        res = 0
        count = [0] * 26
        n = len(s)

        left = 0

        for right in range(n):
            count[ord(s[right])-65] += 1
            sub_freq = max(count)

            # pushing the left pointer 
            while (right - left + 1 - sub_freq > k):
                count[ord(s[left])-65] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res
                


            

        
        