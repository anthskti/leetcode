class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if its rotate only to a certain degree, we can binary search it's rotation pivot
        # then using that pivot, we can just return the pivot
        left = 0
        right = len(nums) -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]: 
                # this means we have a issue, pivot is on left side
                right = mid
            else:
                left = mid + 1

        return nums[left]
            

            
        