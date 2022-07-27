class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counterArray=collections.Counter(changed)
        if counterArray[0]%2:
            return []
        result=[]
        for x in sorted(counterArray):
            if counterArray[x]>counterArray[x*2]:
                return []
            counterArray[x*2]-=counterArray[x] if x!=0 else counterArray[x]//2
            result.append(x)
        return counterArray.elements()
    
        """
        
        a={ y:False for y in changed}
        r=[]
        changed.sort()
        for x in changed:
            if (x%2==1 or x//2 not in a) and x*2 not in a:
                return []
            if x*2 in a and a[x]==False:
                a[x*2]=True
                r.append(x)
        return r
        """