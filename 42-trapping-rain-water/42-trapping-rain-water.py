class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        l_mx=0
        r_mx=0
        res=0
        while l<r:
            if h[l]<h[r]:
                l_mx=max(l_mx, h[l])
                res+=l_mx-h[l]
                l+=1
            else:
                r_mx=max(r_mx, h[r])
                res+=r_mx-h[r]
                r-=1
        return res