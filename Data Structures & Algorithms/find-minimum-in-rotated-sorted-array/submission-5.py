class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if its rotate only to a certain degree, we can binary search it's rotation pivot
        # then using that pivot, we can just return the pivot
        left = 0
        right = len(nums) -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:  
                # if the right side is sorted, then our pivot is on the left side
                right = mid
            else: # if the right side isn't sorted, then our pivot is on the right side
                left = mid + 1

        return nums[left] # left is just our pivot
            

            
        