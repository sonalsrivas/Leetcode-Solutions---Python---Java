class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)
        
        if sumA<sumB:
            a=bobSizes
            b=aliceSizes
            sumA,sumB=sumB,sumA
            revFlag=True
        else:
            a=aliceSizes
            b=bobSizes
            revFlag=False
        
        setA=set(a)
        setB=set(b)
        
        equalSum=(sumA+sumB)//2
        diff=sumA-equalSum
        
        for num in b:
            if num+diff in setA:
                return [num, num+diff] if revFlag else [num+diff, num]