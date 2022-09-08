class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=9
        mapRowNum=[set() for i in range(n)]
        mapColNum=[set() for i in range(n)]
        mapBoxNum=defaultdict(set)
        setEmptySpaces=[]
        for i in range(n):
            for j in range(n):
                if board[i][j]!='.':
                    boxI,boxJ=(i//3)*3,(j//3)*3
                    mapRowNum[i].add(board[i][j])
                    mapColNum[j].add(board[i][j])
                    mapBoxNum[(boxI,boxJ)].add(board[i][j])
                else:
                    setEmptySpaces.append((i,j))
    
        def backtrack(i):
            if i>=len(setEmptySpaces):
                return True
            x,y=setEmptySpaces[i]
            boxX, boxY= ((x//3)*3,(y//3)*3)
            for num in range(1,10):
                num=str(num)
                if num not in mapRowNum[x] and num not in mapColNum[y] and num not in mapBoxNum[(boxX, boxY)]:
                    mapRowNum[x].add(num)
                    mapColNum[y].add(num)
                    mapBoxNum[(boxX, boxY)].add(num)
                    board[x][y]=num
                    res=backtrack(i+1)
                    if res:
                        return True
                    board[x][y]='.'
                    mapRowNum[x].remove(num)
                    mapColNum[y].remove(num)
                    mapBoxNum[(boxX, boxY)].remove(num)
            return False
    
        result=backtrack(0)
        #print(board)
        return result