class Solution:
    def trap(self, height: List[int]) -> int:
        # the question wants the maximum area that can be mad between the number heights

        # my intuitive implementation would be per each height, we can find all empty values between two values, so fix the max lowest and highest value on each height until max. however this os O(n*h)

        # we can actually fill this water by looking at the columns.

        # a brute force way would likely to for every i, find the tallest left and tallest right values, then choose min of those and subtract current block. apply that to the next step, but that's O(n^2) time.

        # we can use two pointer to manage the height points

        # base case
        if len(height) == 0:
            return 0

        res = 0 

        left = 0
        right = len(height)-1

        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            
            # check max sides
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            # condition
            if maxLeft > maxRight: 
                # no if condition after is needed since maxRight is always >= height[right] from out max side check
                res += maxRight - height[right] 
                right -= 1
            else:
                res += maxLeft - height[left] 
                left += 1
        return res


        # Time: O(n), two pointer
        # Space: O(1), only holds 5 vars