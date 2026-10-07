class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # finding the minimumize the max bananas that could be eaten
        # after a certain k, all values will be feasible
        # boundaries of # of bananas eaten within an h 1 to max(piles)

        # our feasibility condition can just look at the ceiling division each pile[i]

        left = 1
        right = max(piles)

        def isFeasible(x):
            total = 0
            for p in piles:
                total += math.ceil(p/x)
            return total <= h


        while (left < right):
            mid = (left + right) // 2
            if isFeasible(mid):
                right = mid
            else: 
                left = mid + 1
        return left
