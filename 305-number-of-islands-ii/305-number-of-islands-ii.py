class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(a):
            if d[a]!=a:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        
        neigh=((-1,0),(0,-1),(0,1),(1,0))
        d={(i,j):(i,j) for i in range(m) for j in range(n)}
        
        count=0
        pool=set()
        res=[]
        for x,y in positions:
            if (x,y) in pool:
                res.append(count)
                continue
            islandNeigh=set()
            for i,j in neigh:
                i+=x; j+=y
                if -1<i<m and -1<j<n and (i,j) in pool:
                    islandNeigh.add((i,j))
                    
            # This means that there are no islands as neighbours of x,y ... 
            # ... so number of islands will increment by one
            if not islandNeigh:
                count+=1
            else:
                uniqueTrees=set()
                for cmp1 in islandNeigh:
                    uniqueTrees.add(find(cmp1))
                    
                for cmp1 in islandNeigh:
                    union(cmp1, (x,y))
                count-=len(uniqueTrees)-1
                
            pool.add((x,y))
            res.append(count)
        return res