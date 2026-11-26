class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return bool, if s2 is a permutation of s1.

        # since we're finding a section of a string, we can look at 
        # sliding window

        # we can track it with some data structure

        # edge case 
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        # initalize target
        for char in s1:
            target[ord(char) - ord('a')] += 1

        # initalize first len(s1)
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
            if target == window:
                return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            window[ord(s2[l]) - ord('a')] -= 1
            window[ord(s2[r]) - ord('a')] += 1
            l += 1
            if target == window:
                return True

        return False
        
    # Time O(n)
    # Space O(26) == O(1)
            
            


        
            
            


            
