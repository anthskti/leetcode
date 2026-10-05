class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # how many car fleets will arroive at the destination
        # we can imagine this like a graph, y: distance, x: hrs
        # the car in the front is always the bottle neck
        # we should be approaching this equation backwards.
        # stack approach: we can take the length of the stack
        # add first position, then 

        pair = [[p,s] for p, s in zip(position, speed)] 

        stack = []
        for p, s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

