class Solution:
    def diagonalSort(self, a: List[List[int]]) -> List[List[int]]:
        n=len(a[0])
        m=len(a)
        
        def sortThisDiagonal(i,j):
            x=i; y=j
            sortSack=[]
            while x<m and y<n:
                sortSack.append(a[x][y])
                x+=1
                y+=1
            sortSack.sort()
            x=i; y=j
            k=0
            while x<m and y<n:
                a[x][y]=sortSack[k]
                x+=1
                y+=1
                k+=1
                
        sortSack=[]
        for j in range(n):
            i=0
            sortThisDiagonal(i,j)
        for i in range(1,m):
            j=0
            sortThisDiagonal(i,j)
        
        return a