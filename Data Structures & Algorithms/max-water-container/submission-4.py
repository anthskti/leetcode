class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # output is max amount of water
        # brute force approach would be O(n^2) time but we could utilize
        # a two pointer approach where we simply check for higher bars
        # A simple way to calc is length x minimum of the two positions

        l = 0
        r = len(heights) - 1
        res = 0
        
        while(l < r):
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res
