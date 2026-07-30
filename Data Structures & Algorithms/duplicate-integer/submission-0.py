class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force is n^2, check each element and compare itself
        # n-logn time where for each element, we binary search a corresponding one
        # n time, where we put it in a hashset, and track it
        
        counter = Counter(nums)

        for i in counter:
            if counter.get(i) > 1:
                return True
            
        return False