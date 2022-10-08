import math
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        def union(a,b):
            d[find(a)]=find(b)
        
        def find(a):
            #print(d,a)
            if d[a]!=a:
                d[a]=find(d[a])
            return d[a]
                
        d=[i for i in range(n+1)]
        
        visited=[0]*(n+1)
        for i in range(threshold+1, n+1):
            if visited[i]==0:
                for j in range(i, n+1, i):
                    union(i,j)
            
        # for i in range(1,n+1):
        #     for j in range(i+1, n+1):
        #         if math.gcd(i,j)>threshold:
        #             union(i,j)
        
        k=0
        result=[False]*len(queries)
        for a,b in queries:
            parent_a=find(a)
            parent_b=find(b)
            result[k] = parent_a==parent_b
            k+=1
        return result