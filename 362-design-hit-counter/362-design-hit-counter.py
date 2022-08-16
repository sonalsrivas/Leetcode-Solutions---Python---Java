class HitCounter:

    def __init__(self):
        self.q=deque()
        self.hitsInLast300secs=0

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        self.hitsInLast300secs+=1

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0]+300<=timestamp:
            self.q.popleft()
            self.hitsInLast300secs-=1
        return self.hitsInLast300secs


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)