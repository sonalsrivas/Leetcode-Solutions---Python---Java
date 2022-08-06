class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.map:
            indexToInsert = self.binarySearchSmallerOrEqual(self.map[key], timestamp) + 1

            self.map[key].insert(indexToInsert, (timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            indexClosest = self.binarySearchSmallerOrEqual(self.map[key], timestamp)
        else:
            return ''
        return self.map[key][indexClosest][1] if -1 < indexClosest < len(self.map[key]) else ''

    @staticmethod
    def binarySearchSmallerOrEqual(keyMap, timestamp):
        left = 0
        right = len(keyMap) - 1
        if timestamp >= keyMap[right][0]:
            return right
        if timestamp < keyMap[left][0]:
            return left - 1
        while left < right - 1:

            mid = (left + right) // 2
            if keyMap[mid][0] > timestamp:
                right = mid - 1

            elif keyMap[mid][0] == timestamp:
                return mid
            else:
                left = mid
        return left