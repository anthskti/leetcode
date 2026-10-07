class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set two pointers: left and right
        # ignore all non ascii values
        # two ways: compare ascii values or set lower

        # edge case
        if len(s) < 2:
            return True

        # s = s.lower() # O(n) time

        left = 0
        right = len(s) - 1

        def is_valid(x):
            return (97 <= x <= 122) or (48 <= x <= 57)          

        while left < right:
            l = ord(s[left].lower())
            r = ord(s[right].lower())

            # check if a valid ascii value
            if not is_valid(l):
                left += 1
                continue
            if not is_valid(r):
                right -= 1
                continue

            
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1

        return True

        