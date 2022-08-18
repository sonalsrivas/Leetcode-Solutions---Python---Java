class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x+1
        while l+1<r:
            m=(l+r)//2
            c=m*m
            if c<x:
                l=m
            elif x<c:
                r=m
            else:
                return m
        return l