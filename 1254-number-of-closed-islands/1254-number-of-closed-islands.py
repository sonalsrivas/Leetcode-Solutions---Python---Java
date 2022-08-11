import queue
class Solution:
    noOfClosedIslands=0
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        # If 0 in the island touches the border, it is a done game for the island.
        m=len(grid)
        n=len(grid[0])
        neighbours=((-1,0),(1,0),(0,-1),(0,1))
        self.noOfClosedIslands=0
        
        def BFS(i,j,m,n):
            closedIslandFlag=1
            q=queue.Queue()
            q.put((i,j))
            while not q.empty():
                x,y=q.get()
                grid[x][y]=1
                for g,h in neighbours:
                    g+=x; h+=y
                    if -1<g<m and -1<h<n:
                        if grid[g][h]==1:
                            pass
                        else:
                            q.put((g,h))
                    else:
                        closedIslandFlag=0
                        
            return closedIslandFlag

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    self.noOfClosedIslands+=BFS(i,j,m,n)
        return self.noOfClosedIslands
    
"""
[
[0,0,1,1,0,1,0,0,1,0],
[1,1,0,1,1,0,1,1,1,0],
[1,0,1,1,1,0,0,1,1,0],
[0,1,1,0,0,0,0,1,0,1],
[0,0,0,0,0,0,1,1,1,0],
[0,1,0,1,0,1,0,1,1,1],
[1,0,1,0,1,1,0,0,0,1],
[1,1,1,1,1,1,0,0,0,0],
[1,1,1,0,0,1,0,1,0,1],
[1,1,1,0,1,1,0,1,1,0]
]
"""