import heapq
def binarySearch(a,t, price):
    n=len(a)
    l=0
    r=n-1
    while l<r:
        m=(l+r)//2
        if a[m][0]<t:
            l=m+1
        else:
            r=m
    return l

class StockPrice:

    def __init__(self):
        self.max=[]
        self.min=[]
        heapq.heapify(self.max)
        heapq.heapify(self.min)
        self.record=[]
        self.tp=dict()

    def update(self, timestamp: int, price: int) -> None:
        
        self.tp[timestamp]=price
        a=self.record
        n=len(a); t=timestamp
        l=binarySearch(self.record, timestamp, price)
        #self.record.insert(indexToInsertIn, [timestamp, price])
        if l<n and a[l][0]==t:
            a[l][1]=price
                
        elif l<n and a[l][0]>=t:
            a.insert(l, [t,price])
        else:
            a.append([t,price])
        heapq.heappush(self.max, (-price, timestamp))
        heapq.heappush(self.min, (price, timestamp))
        #print(self.record, self.max, self.min)

    def current(self) -> int:
        return self.record[-1][1]

    def maximum(self) -> int:
        p,t=p,t=self.max[0]#heapq.heappop(self.max)
        while -self.tp[t]!=p:
            heapq.heappop(self.max)
            p,t=self.max[0]
            """if t not in tp:
                heapq.heappop(self.max) 
                p,t=self.max[0]"""
        return -p

    def minimum(self) -> int:
        p,t=self.min[0]#heapq.heappop(self.min)
        while self.tp[t]!=p:
            heapq.heappop(self.min)
            p,t=self.min[0]
            """if t not in tp:
                heapq.heappop(self.min) 
                p,t=self.min[0]"""
        return p


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()