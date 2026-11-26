class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return an int of the longest string
        # misunderstood the question

        # requires O(n) time, cant sort
        # inuition, sort, and check if neighbour is larger. finding largest. 
        # var max and track
        max_count = 0
        seq = set()

        lookup = set(nums)
        for num in lookup:
            if num - 1 not in lookup:
                seq.add(num)

        for key in seq:
            count = 1
            temp_num = key + 1
            while (temp_num in lookup):
                count += 1
                temp_num += 1
            max_count = max(max_count, count)

        return max_count

        # Time O(n)
        # Space O(n)
        
        