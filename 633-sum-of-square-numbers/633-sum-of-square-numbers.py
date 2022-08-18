class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def sqRootBinSearch(x):
            if x<2:
                return x
            l=0
            r=x//2+1
            while l+1<r:
                m=(l+r)//2
                candi=m*m
                if candi<x:
                    l=m
                elif candi>x:
                    r=m
                else:
                    return m
            return l
        l=0
        r=sqRootBinSearch(c)
        while l<=r:
            y=l*l+r*r
            if y>c:
                r-=1
            elif y<c:
                l+=1
            else:
                return True
        return False