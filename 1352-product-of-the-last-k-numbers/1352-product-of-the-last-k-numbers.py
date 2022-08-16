class ProductOfNumbers:

    def __init__(self):
        self.q=deque([1])
        self.zeroIndx=[]
        self.index=0
        self.prod=1

    def add(self, num: int) -> None:
        
        if num==0:
            self.zeroIndx.append(self.index)
            self.q.clear()
            self.prod=1
        else:
            self.prod*=num
        self.q.append(self.prod)
        self.index+=1

    def getProduct(self, k: int) -> int:
        if self.zeroIndx and self.zeroIndx[-1]+k>=self.index:
            return 0
        return self.prod//self.q[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)