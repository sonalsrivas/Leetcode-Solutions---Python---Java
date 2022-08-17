class Solution:
    def __init__(self):
        self.d=[1]*100
        self.d[0]=0
        for i in range(2,100,2):
            self.d[i]=self.d[i//2]
            j=i+1
            self.d[j]=self.d[j//2]+self.d[j//2+1]
        #for j in range(1,100,2):
        #    self.d[j]=self.d[j//2]+self.d[j//2+1]
        
    def getMaximumGenerated(self, n: int) -> int:
        return max(self.d[:n+1])