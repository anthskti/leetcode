class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force: at each i, we loop through until we see a value > i, its O(n2) though
        # How to incorporate stack in this solution?
        # goal: O(n) time O(n) space
        # for temperatures[i], for each i, we append(?)
        # we go backwards and compute the values behind it. 

        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: 
                s_t, s_i = stack.pop()
                res[s_i] = (i - s_i)
            
            stack.append([t, i])
        
        return res


        
        