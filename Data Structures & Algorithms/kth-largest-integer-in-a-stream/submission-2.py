import heapq

class KthLargest:
    # O(n) Space

    def __init__(self, k: int, nums: List[int]):
        # O(n) time 
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        # O(logk) time
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

        return self.heap[0]
        
