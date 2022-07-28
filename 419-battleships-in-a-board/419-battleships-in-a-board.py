class Solution:
    def countBattleships(self, a: List[List[str]]) -> int:
        m=len(a)
        n=len(a[0])
        count=0
        for i in range(m):
            for j in range(n):
                if a[i][j]=='X':
                    if (j==n-1 or a[i][j+1]=='.') and (i==m-1 or a[i+1][j]=='.'):
                        count+=1
        return count