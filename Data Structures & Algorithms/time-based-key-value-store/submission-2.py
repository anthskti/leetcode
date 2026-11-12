class TimeMap:
    # since we ar working with key-value pairs, a hash map is appropriate

    def __init__(self):
        self.time_map = {} # string: [string, int] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # We just return the most recent one
        res = ""
        values = self.time_map.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= values[m][1]:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1


        
        return res
        
        # Get: Time O(logn), we use binary search organized automatically by time
        # Set: Time O(1), hashmap insert
        # Space O(n), hashmap
        
