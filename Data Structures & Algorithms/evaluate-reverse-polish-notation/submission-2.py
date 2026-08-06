class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Utilizing a stack, we can pop our most recent value st

        # have a res that holds all the information
        # we add to stack, the pop last two (doing arithmetic) when arithmetic is added

        stack = []

        for c in (tokens):
            if c == "+": 
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop() 
                b = stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a = stack.pop() 
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]

                


            