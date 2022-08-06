class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.map:
            indexToInsert = self.binarySearch(self.map[key], timestamp) + 1

            self.map[key].insert(indexToInsert, (timestamp, value))

        else:
            self.map[key] = [(timestamp, value)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            indexClosest = self.binarySearch(self.map[key], timestamp)
            #if self.map[key][indexClosest][0] > timestamp:
            #    return ''
        else:
            return ''
        return self.map[key][indexClosest][1] if -1<indexClosest < len(self.map[key]) else ''

    def binarySearch(self, kmap, timestamp):
        l = 0
        r = len(kmap) - 1
        if timestamp >= kmap[r][0]:
            return r
        if timestamp < kmap[l][0]:
            return l-1
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

