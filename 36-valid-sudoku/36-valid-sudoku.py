class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9
        mapRowNum=[set() for i in range(n)]
        mapColNum=[set() for i in range(n)]
        mapBoxNum=defaultdict(set)
        for i in range(n):
            for j in range(n):
                if board[i][j]!='.':
                    boxI,boxJ=(i//3)*3,(j//3)*3
                    if board[i][j] in mapRowNum[i] or board[i][j] in mapColNum[j] or board[i][j] in mapBoxNum[(boxI,boxJ)]:
                        return False
                    mapRowNum[i].add(board[i][j])
                    mapColNum[j].add(board[i][j])
                    mapBoxNum[(boxI,boxJ)].add(board[i][j])
        return True