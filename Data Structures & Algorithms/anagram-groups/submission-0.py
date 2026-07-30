class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: List word
        # Output: list of list that group have the exact same content (unorganized)

        # Time complexity: O(nlogn x m)?
        # sort each string, then put them into a hash map, -> using main strs, append according to new list
        # Space complexity: O(n)

        res = defaultdict(list)

        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            res[sorted_str].append(strs[i]) # appends if not there, skips if is
        return list(res.values())


        