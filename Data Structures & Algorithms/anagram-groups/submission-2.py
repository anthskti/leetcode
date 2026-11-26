class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output is a anagrams listed together

        # we can make a hashmap, having the keys as sorted string
        # then we compare whether they exist and add it or don't and new list it

        anagrams = {} # key: value -> "str": "str"

        for s in strs:
            word = str(sorted(s))
            if word not in anagrams:
                anagrams[word] = []
            anagrams[word].append(s)
        
        # make it into a list
        res = []
        for key, value in anagrams.items():
            res.append(value)

        return res
    # Time O(n * slogs) where n is the length of the list ands is the length of the longest string
    # Space O(n)

        