class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of integers, some integer k 
        # output, the top k integers. 

        # Time: O(N); hash, count total. then sort decending and append to list. 

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        r_sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        
        res = list(r_sorted_count.keys())


        return res[0:k]