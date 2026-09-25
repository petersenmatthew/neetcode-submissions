class TimeMap:
    # underlyingds: a hash map w/ a tuple?
    # (key, timestamp) : value?

    # key -> [(timestamp, value), (timestamp, value)...]
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add timestamp value to this key
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values_list = self.map[key]
        target = timestamp
        left = 0
        right = len(values_list) - 1
        best = ""
        # values_list: [(1, happy), (2, sad), (3, neutral)]
        while left <= right:
            mid = (left + right) // 2

            if target == values_list[mid][0]:
                return values_list[mid][1]
            elif target <= values_list[mid][0]:
                right = mid - 1
            else:
                best = values_list[mid][1]
                left = mid + 1 
        return best

         
        
