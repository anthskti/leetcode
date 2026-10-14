class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # output: a list of pairs, where the pairs are merged from intervals 
        # we sort the intervals based on the first value. 
        # then we check overlap

        # Time O(nlogn) space O(n)
        
        intervals.sort(key=lambda i : i[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            lastOutput = output[-1][1]
            if (intervals[i][0] <= lastOutput) :
                output[-1][1] = max(intervals[i][1], output[-1][1])
                # case [1,5],[2,4]; adding max avoids shrinking
            else:
                output.append(intervals[i])
        
        return output

