import heapq


class StockPrice:

    def __init__(self):
        self.max = []
        self.min = []
        heapq.heapify(self.max)
        heapq.heapify(self.min)
        self.latestTimestamp = 0
        self.timestampPrice = dict()

    def update(self, timestamp: int, price: int) -> None:
        self.timestampPrice[timestamp] = price
        self.latestTimestamp = max(self.latestTimestamp, timestamp)
        heapq.heappush(self.max, (-price, timestamp))
        heapq.heappush(self.min, (price, timestamp))

    def current(self) -> int:
        return self.timestampPrice[self.latestTimestamp]

    def maximum(self) -> int:
        maxPrice, corTime = self.max[0]
        while -self.timestampPrice[corTime] != maxPrice:
            heapq.heappop(self.max)
            maxPrice, corTime = self.max[0]
        return -maxPrice

    def minimum(self) -> int:
        minPrice, corTime = self.min[0]
        while self.timestampPrice[corTime] != minPrice:
            heapq.heappop(self.min)
            minPrice, corTime = self.min[0]
        return minPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
