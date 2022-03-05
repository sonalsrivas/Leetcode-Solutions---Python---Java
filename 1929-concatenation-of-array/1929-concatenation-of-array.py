class Solution:
    def getConcatenation(self, m: List[int]) -> List[int]:
        n=len(m)
        a=[0]*2*n
        for i in range(n):
            a[i]=m[i]
            a[i+n]=m[i]
        return a