class Solution:
    def numberOfBeams(self, a: List[str]) -> int:
        m=len(a)
        n=len(a[0])
        laserBeamCount=0
        prev=0
        for row in a:
            oneCount=row.count('1')
            if oneCount>0:
                laserBeamCount+=oneCount*prev
                prev=oneCount
        return laserBeamCount