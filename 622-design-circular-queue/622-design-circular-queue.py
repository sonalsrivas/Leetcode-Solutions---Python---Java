class MyCircularQueue:
    def __init__(self, k: int):
        self.k=k
        self.cq=[None]*k
        self.pointer=0
        self.beg=0
        self.cap=0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cq[self.pointer]=value
        self.pointer=(self.pointer+1)%self.k
        self.cap+=1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.cq[self.beg]=None
        self.beg=(self.beg+1)%self.k
        self.cap-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.beg]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[(self.pointer-1)%self.k]

    def isEmpty(self) -> bool:
        return self.cap==0
    
    def isFull(self) -> bool:
        return self.cap==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()