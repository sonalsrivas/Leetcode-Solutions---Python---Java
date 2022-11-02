class MedianFinder:

    def __init__(self):
        self.smallerHalfInMaxHeap=[]
        self.greaterHalfInMinHeap=[]
        

    def addNum(self, num: int) -> None:
            
        heappush(self.smallerHalfInMaxHeap, -num)
        maximumNumberFromSmallerHalf = -heappop(self.smallerHalfInMaxHeap)
            
        heappush(self.greaterHalfInMinHeap, maximumNumberFromSmallerHalf)
        
        if len(self.smallerHalfInMaxHeap) < len(self.greaterHalfInMinHeap):   
            
            minimumNumberFromGreaterHalf = heappop(self.greaterHalfInMinHeap)
            
            heappush(self.smallerHalfInMaxHeap, -minimumNumberFromGreaterHalf)

    def findMedian(self) -> float:
        if len(self.smallerHalfInMaxHeap) == len(self.greaterHalfInMinHeap):
            return (-self.smallerHalfInMaxHeap[0] + self.greaterHalfInMinHeap[0])/2
        return -self.smallerHalfInMaxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()