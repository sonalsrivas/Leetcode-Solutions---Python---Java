class HitCounter:

    def __init__(self):
        self.q=deque()
        self.hitsInLast300secs=0

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        self.hitsInLast300secs+=1
        # print(self.q, self.q[0]+300,timestamp)
        # while self.q[0]+300<timestamp:
        #     print(self.q[-1])
        #     self.q.popleft()
        #     self.hitsInLast300secs-=1

    def getHits(self, timestamp: int) -> int:
        #print("***getHits*** ",self.q,self.q[0]+300, timestamp)
        while self.q and self.q[0]+300<=timestamp:
            print("reduced",self.hitsInLast300secs)
            print(self.q[-1])
            self.q.popleft()
            self.hitsInLast300secs-=1
        return self.hitsInLast300secs


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)