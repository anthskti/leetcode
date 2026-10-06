class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maximize rectangle size

        # I think a brute force approach is to check every position n, then calc the max rectangle via n runs. but that's O(n^2)
        # I better approach is likely to use some sort of stack since this is a subarray solution.

        # to check largest rectangle, we have to look if heights[i] > heights[i+1], since a larger rectangle cannot be computed if that conditions hits.
        # we can have a stack that tracks this instance.
        max_area = 0
        stack = []
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ind, hei = stack.pop()

                area = (i - ind) * hei
                if max_area < area:
                    max_area = area
                start = ind

            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))


        return max_area