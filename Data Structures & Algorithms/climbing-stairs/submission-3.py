class Solution:
    def climbStairs(self, n: int) -> int:
        # output: the number if distinct ways to climb stairs
        # this is a fibonacci sequence type questionw here we can utilize the previous values to climb up to our current answer
        # there is also a way to make this space O(1) by just adding instead of using alist to keep track of all values
        # Time complexity is O(n)

        if n == 1:
            return 1
        if n == 2:
            return 2
            
        first = 1
        second = 2

        for i in range(2, n):
            count = first + second
            if i % 2 == 0:
                first = count 
            else:
                second = count
        

        return count
