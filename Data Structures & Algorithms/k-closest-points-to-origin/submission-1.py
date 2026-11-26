import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return the k closest point to the origin 0,0

        # we can can create a min heap, storing the euclidean distance + the cord
        # then loop k popping the min element.

        heap = []
        for x,y in points:
            e = (x-0)**2 + (y-0)**2 # i don't even need to sqrt xD
            heap.append((e, [x,y]))
        
        heapq.heapify(heap)

        res = []
        for i in range(k):
            e, coord = heapq.heappop(heap)
            res.append(coord)
        
        return res

        # Time O(n (logk+1)), n is len(points), k is k 
        # Space O(n)