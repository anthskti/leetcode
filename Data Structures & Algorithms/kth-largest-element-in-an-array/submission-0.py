import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return the kth largest element
        # unsorted array
        # use a bounded heap
        heap = nums.copy()
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]

    # Time O(n + n-k (logk))
    # Space O(n)


        