class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l=1
        r=num//2+1
        while l+1<r:
            m=(l+r)//2
            c=m*m
            if c<num:
                l=m
            elif c>num:
                r=m
            else:
                return True
        return False
        