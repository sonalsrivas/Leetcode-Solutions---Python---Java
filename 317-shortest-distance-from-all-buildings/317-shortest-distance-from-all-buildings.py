from collections import deque


class Solution:
    def shortestDistance(self, grid):
        m=len(grid)
        n=len(grid[0])
        neighbours=((-1,0),(1,0),(0,1),(0,-1))
        relevantHousingCellsMapDistance=dict()
        def BFSbuildingToHousingCells(x,y, relevantHousingCellsMapDistance):
            #print("BFSing for buidling:: ", x,y, relevantHousingCellsMapDistance)
            relevantHousingCellsMapDistance_temp=dict()
            q=deque()
            q.append((x,y,0))
            level=0
            while q:
                i,j,level = q.popleft()
                for v,w in neighbours:
                    v+=i; w+=j
                    #print(v,w,relevantHousingCellsMapDistance,relevantHousingCellsMapDistance_temp)
                    if -1<v<m and -1<w<n and grid[v][w]==0 and (v,w) in relevantHousingCellsMapDistance and (v,w) not in relevantHousingCellsMapDistance_temp:
                        q.append((v,w,level+1))
                        #distance=abs(x-v)+abs(y-w)
                        distance=level+1
                        relevantHousingCellsMapDistance_temp[(v,w)]=relevantHousingCellsMapDistance[(v,w)]+distance
                #q.append((-1,-1))
            #print("returning follwing:, ",relevantHousingCellsMapDistance_temp)
            return relevantHousingCellsMapDistance_temp

        setBuildingPositions=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    setBuildingPositions.add((i,j))
                elif grid[i][j]==0:
                    relevantHousingCellsMapDistance[(i,j)]=0
        for k,l in setBuildingPositions:
            relevantHousingCellsMapDistance=BFSbuildingToHousingCells(k,l, relevantHousingCellsMapDistance)
        return min(relevantHousingCellsMapDistance.values()) if relevantHousingCellsMapDistance else -1