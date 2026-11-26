class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # output: list of the top k most frequent numbers
        
        # count them using a hashmap to track the numbers and the amount of them
        
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        # append list, sort the list reversed, and parse only 0 - k
        return sorted(list(count.keys()), key=lambda x: count[x], reverse=True)[:k]

        # O(n + nlogn) -> O(nlogn) Time
        # O(n) Spcae
