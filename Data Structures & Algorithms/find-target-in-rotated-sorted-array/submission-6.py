class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the array is already sorted
        # Sure we could just resort it, but i'll be O(nlogn)
        # we can just go through the array, but that'd be O(n)
        # we could likely use binary search O(logn) since we're just searching for the array.
        # I think the best way we can go about this is finding at what point its sorted, then using that position as an index, we can binary search on those conditions.

        # there will be two conditionals. if our middle value is bigger than our left value, we know it belongs to the left sorted half. 
        # if the middle value is smaller than the right value, we know it belongs to the right sorted half.

        # search for the beginning position, so we can calc rotation
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: 
                return mid

            # Search the left 
            if nums[left] <= nums[mid]: 
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # Search the right
            else: 
                if nums[mid] < nums[right]:
                    if target < nums[mid] or nums[right] < target:
                        right = mid - 1
                    else: 
                        left = mid + 1
        return -1 



