class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want to return a list of all triplets that add up to the sum 0 
        # brute force approach, O(n^3)
        # two pointer approach?
        # our approach will look for every n[i] we do a two pointer approach to find two other values in n to get a triplet

        # O(n^2) time as n for first hard search in array and n for two pointer
        # O(n) space for the result

        nums.sort()

        triplet = []
        n = len(nums)
        
        for i in range(n-2):
            # three positions after some positive cannot be zero
            if nums[i] > 0:
                break

            # skips dups
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else: # val == 0
                    triplet.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # we already made the move so we have to check left-1 and right+1 respectively
                    while (left < right and nums[left] == nums[left - 1]):
                        left +=1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -=1

        return triplet

                