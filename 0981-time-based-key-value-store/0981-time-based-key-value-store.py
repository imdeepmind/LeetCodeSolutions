class TimeMap:

    def __init__(self):
        self.cache = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.cache:
            self.cache[key].append((value, timestamp))
        else:
            self.cache[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache: return ""

        items = self.cache[key]

        l, r = 0, len(items) - 1
        res = -1

        while l <= r:
            m = l + ((r-l)//2)

            if items[m][1] == timestamp:
                res = m
                break
            
            if items[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
                res = m

        return items[res][0] if res != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)