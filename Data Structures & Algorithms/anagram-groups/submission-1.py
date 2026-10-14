class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output requires grouping/listing up anagrams and returning a list of all. 
        # using a hash map, we can start at 0, sort it, then make it its key, and add the unsorted version as its value. we do this for each value. 
        # we can then return the values afterwards

        count = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            count[sorted_s].append(s)
        
        res = []
        for k,v in count.items():
            res.append(v)
        return res
            
            



        