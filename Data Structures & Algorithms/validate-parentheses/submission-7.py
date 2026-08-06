class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time, read through list
        #( 
        
        # Speed case: can't be valid is string is not even
        if len(s) % 2 != 0: return False

        stack = []
        
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])

            elif stack:
                if s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                else: 
                    return False
            else:
                return False

        if not stack: 
            return True 
        
        return False