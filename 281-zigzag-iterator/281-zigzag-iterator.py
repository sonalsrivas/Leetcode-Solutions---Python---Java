class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1=deque(v1)
        self.v2=deque(v2)
        self.cur=1

    def next(self) -> int:
        self.cur^=1
        if self.cur==0:
            if self.v1:
                return self.v1.popleft()
            else:
                return self.v2.popleft()
            self.cur=1
        else:
            if self.v2:
                return self.v2.popleft()
            elif self.v1:
                return self.v1.popleft()
            self.cur=0

    def hasNext(self) -> bool:
        return self.v1 or self.v2

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())