class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return the exclusive non-overlapping interval list

        # logical intuition
        # we have to sort by intervals[i][0] 
        # then with the list, we check intervals[i][1] and pass all intervals[i+1][0] that are smaller, setting the max(intervals[i][1] and intervals[i+1])
        # until there exist more smaller ones, then we move on and append.
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals.sort(key=lambda x: x[0]) # x represents the key

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res

        # Time O(nlogn)
        # Space O(n)


        
