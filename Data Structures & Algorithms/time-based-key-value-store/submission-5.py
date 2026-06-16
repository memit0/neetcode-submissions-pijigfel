class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        search_array = self.hashmap[key]
        l, r = 0, len(search_array) - 1

        res = ""

        while l <= r:
            mid = (l + r) // 2
            if search_array[mid][0] == timestamp:
                return search_array[mid][1]
            elif search_array[mid][0] <= timestamp:
                res = search_array[mid][1] # Keeping track of the res that is lower than timestamp
                l = mid + 1
            else: 
                r = mid - 1 


        return res

        
