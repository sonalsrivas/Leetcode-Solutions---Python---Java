class Solution:
    def canReorderDoubled(self, a: List[int]) -> bool:
        ac=Counter(a)
        for i in sorted(ac,key=abs):
            if i==0:
                if ac[i]%2==0:
                    continue
                else:
                    return False
            if ac.get(i,0)!=0 and ac.get(i*2,0)!=0:        # i*2 exists
                mc=min(ac[i],ac[i*2])
                ac[i]-=mc
                ac[i*2]-=mc
            
            if ac.get(i,0)!=0:
                return False
        return True