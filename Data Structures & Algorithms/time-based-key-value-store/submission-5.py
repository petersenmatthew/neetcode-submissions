class TimeMap:

    def __init__(self):
        self.map = {}
        # key -> value
        # key -> [(timestamp, value). ...]
        # matthew -> [(2341, boy), (2344, girl)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search for it
        if key not in self.map:
            return ""
        left = 0
        right = len(self.map[key]) - 1
        best = None
        while left <= right:
            mid = (left + right) // 2
            if self.map[key][mid][0] == timestamp:
                return self.map[key][mid][1]
            elif timestamp > self.map[key][mid][0]:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        if best is None:
            return ""
        return self.map[key][best][1]