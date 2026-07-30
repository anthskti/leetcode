class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # With O(n) space, I could make a hash map.
        # or, I could make a list 

        dup = set()
        for num in nums:
            if num in dup:
                return num
            dup.add(num)
        return -1


        