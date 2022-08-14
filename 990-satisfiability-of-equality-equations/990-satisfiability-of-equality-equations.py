import string
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(a):
            if a!=d[a]:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        
        d={i:i for i in string.ascii_lowercase}
        
        for eq in equations:
            u,op,v=eq[0],eq[1],eq[3]
            if op=='=':
                union(u,v)
        for eq in equations:
            u,op,v=eq[0],eq[1],eq[3]
            if op=='!':
                # if u and v are connected by virtue of == operation, this one is a voilation of the same.
                if find(u)==find(v):
                    return False
        return True
        
        