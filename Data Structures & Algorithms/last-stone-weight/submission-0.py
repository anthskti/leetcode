import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]

        heapq.heapify(heap)

        while (len(heap) > 1):
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            z = x - y
            if z != 0:
                heapq.heappush(heap, z)


        if len(heap) == 0:
            return 0
        return -heap[0]

    # Time O(n) initializing
    # Space O(n)

        