class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.map:
            # print("Key map before insertion +++> ", self.map[key])
            indexToInsert = self.binarySearch(self.map[key], timestamp) + 1

            self.map[key].insert(indexToInsert, (timestamp, value))

        else:
            self.map[key] = [(timestamp, value)]
        # print("Key map after insertion +++> ", self.map[key])

    def get(self, key: str, timestamp: int) -> str:
        # print("Looking for ts=> ", timestamp, " Key map +++> ", self.map[key])
        if key in self.map:
            # print(f"{key} and {timestamp} not there@@==!!!")
            indexClosest = self.binarySearch(self.map[key], timestamp)
            # print("indexClosest **> ", indexClosest)
            if self.map[key][indexClosest][0] > timestamp:
                return ''
        else:
            return ''
        return self.map[key][indexClosest][1] if indexClosest < len(self.map[key]) else ''

    def binarySearch(self, kmap, timestamp):
        l = 0
        r = len(kmap) - 1
        if timestamp >= kmap[r][0]:
            return r
        if timestamp < kmap[l][0]:
            return l
        while l < r - 1:

            m = (l + r) // 2
            # print(l, r, m)
            if kmap[m][0] > timestamp:
                r = m - 1
            elif kmap[m][0] == timestamp:
                return m
            else:
                l = m

        return l
