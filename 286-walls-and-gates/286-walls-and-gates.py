class Solution:
    def wallsAndGates(self, rooms):
        def DFS(x,y,dist=0):
            rooms[x][y]=dist
            neighbours=((0,-1),(0,1),(-1,0),(1,0))

            for i,j in neighbours:
                i+=x; j+=y
                if not (-1<i<m and -1<j<n) or rooms[i][j]==-1:
                    continue
                elif rooms[i][j]>dist+1:
                    DFS(i,j,dist+1)
        m=len(rooms)
        n=len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    DFS(i,j)

