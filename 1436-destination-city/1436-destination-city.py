class Solution:
    def destCity(self, a: List[List[str]]) -> str:
        d={u:v for u,v in a}
        
        u,v = d.popitem()
        while True:
            print(u,v)
            if v not in d:
                return v
            u=v
            v=d[u]