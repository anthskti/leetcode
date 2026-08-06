class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Utilizing a stack, we can pop our most recent value st

        # have a res that holds all the information
        # we add to stack, the pop last two (doing arithmetic) when arithmetic is added

        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+": 
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                a = stack.pop() 
                b = stack.pop()
                stack.append(b - a)
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                a = stack.pop() 
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

                


            