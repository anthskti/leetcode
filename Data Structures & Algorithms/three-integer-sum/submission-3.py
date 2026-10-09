class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want to return a list of all triplets that add up to the sum 0 
        # brute force approach, O(n^3)
        # two pointer approach?
        # our approach will look for every n[i] we do a two pointer approach to find two other values in n to get a triplet

        # O(n^2) time as n for first hard search in array and n for two pointer
        # O(n) space for the result

        nums = sorted(nums)

        triplet = []
        n = len(nums)
        
        for i in range(n-2):
            left = i + 1
            right = n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    trip = [nums[i], nums[left], nums[right]]
                    if trip not in triplet:
                        triplet.append(trip)
                    left += 1
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
                

        return triplet


        # [-2,-1,0,1,2,3]
        # -2,-1
                