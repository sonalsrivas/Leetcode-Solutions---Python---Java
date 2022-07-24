class Solution:
    def maxPoints(self, a: List[List[int]]) -> int:
        nr=len(a)
        nc=len(a[0])
        
        p=[0]*nc
        for row in a:
            for j in range(1,nc):
                p[j]=max(p[j], p[j-1]-1)
            for j in range(nc-2, -1,-1):
                p[j]=max(p[j],p[j+1]-1)
            curr=[x+y for x,y in zip(row, p)]
            p=curr
        return max(p)