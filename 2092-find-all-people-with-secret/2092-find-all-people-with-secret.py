class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def find(a):
            if d[a]!=a:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        def isConnected(a,b):
            return find(a)==find(b)
        
        mapTimeEdges=defaultdict(list)
        for u,v,t in meetings:
            mapTimeEdges[t].append((u,v))
        
        SecretPossessor=[0]*n
        SecretPossessor[0]=1
        SecretPossessor[firstPerson]=1
        
        d=[i for i in range(n)]
        union(0,firstPerson)
        
        for time in sorted(mapTimeEdges):
            pool=set()
            for edge in mapTimeEdges[time]:
                u,v=edge
                union(u,v)
                pool.add(u)
                pool.add(v)
            for person in pool:
                if isConnected(0,person):
                    SecretPossessor[person]=1
                else:
                    d[person]=person
                
        return [i for i in range(n) if SecretPossessor[i]==1]