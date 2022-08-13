class Solution:
    def findMissingRanges(self, a: List[int], lower: int, upper: int) -> List[str]:
        low=lower-1
        res=[]
        for i in a:
            if low+1<i-1:
                res.append(str(low+1)+"->"+str(i-1))
            elif low+1==i-1:
                res.append(str(low+1))
            low=i
        if low+1<upper:
            res.append(str(low+1)+"->"+str(upper))
        elif low+1==upper:
            res.append(str(low+1))
        return res