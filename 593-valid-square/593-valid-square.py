class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1==p2 or p2==p3 or p1==p3 or p4==p2 or p4==p1 or p3==p4:
            return False
        def distanceBetween(m,n):
            return ((m[0]-n[0])**2+(m[1]-n[1])**2)
        def computeDiagDist(d):
            return d*2
        def checkFromPoint(p, a,b,c):
            da=distanceBetween(p,a)
            db=distanceBetween(p,b)
            dc=distanceBetween(p,c)
            
            if da==db and dc==computeDiagDist(da):
                    return True
            elif da==dc and db==computeDiagDist(da):
                    return True
            elif db==dc and da==computeDiagDist(db):
                    return True
            return False
        return checkFromPoint(p1,p2,p3,p4) and checkFromPoint(p4,p1,p3,p2)