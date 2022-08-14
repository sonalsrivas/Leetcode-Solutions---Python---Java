class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # find the islands and their area
        def find(a):
            if d[a]!=a:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        
        n=len(grid)
        neigh=((0,1),(1,0)) #(-1,0),(0,-1),
        d={(i,j):(i,j) for i in range(n) for j in range(n) if grid[i][j]==1}
        
        count=0
        pool=set()
        res=[]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    area=1
                    for x,y in neigh:
                        x+=i; y+=j
                        if -1<x<n and -1<y<n and grid[x][y]==1:
                            union((i,j),(x,y))
                            area+=1
        #print(d)
        for i,j in d:
            find((i,j))
        #print(d)
        
        # find areas of all the islands
        mapArea=Counter(list(d.values()))
        #print(mapArea)
        
        neigh=((0,1),(1,0),(-1,0),(0,-1))
        # find the largest area 0 point
        if mapArea:
            largestPossibleIsland=max(mapArea.values())
        else:
            return 1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    islandNeigh=set()
                    for x,y in neigh:
                        x+=i; y+=j
                        if -1<x<n and -1<y<n and grid[x][y]==1:
                            islandNeigh.add(d[(x,y)])
                    #sm=1
                    #for p in islandNeigh:
                    #    print(p)
                    largestPossibleIsland=max(largestPossibleIsland, sum(mapArea[d[p]] for p in islandNeigh)+1)    
                    
        return largestPossibleIsland
""" 
[[1,1,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[1,1,0,0,0],[0,1,0,1,0]]
"""