class Solution:
    def gameOfLife(self, a: List[List[int]]) -> None:
        m=len(a)
        n=len(a[0])
        nei=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                for x,y in ((-1,-1),(-1,1),(-1,0), (0,-1), (0,1),(1,-1),(1,1), (1,0)):
                    x+=i
                    y+=j
                    if -1<x<m and -1<y<n and a[x][y]==1:
                        nei[i][j]+=1
        for i in range(m):
            for j in range(n):
                if a[i][j]==1 and nei[i][j]<2:
                    a[i][j]=0
                elif a[i][j]==1 and nei[i][j]>3:
                    a[i][j]=0
                elif a[i][j]==0 and nei[i][j]==3:
                    a[i][j]=1