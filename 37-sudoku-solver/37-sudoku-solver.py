class Solution:
    
    from collections import defaultdict 
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def findTheBox(i,j):
            return ((i//3)*3, (j//3)*3)

    
        n=9
        setOfDigitsInRow = defaultdict(set) # key: row number .... value: set of digits in that row
        setOfDigitsInCol = defaultdict(set)
        setOfDigitsInBox = defaultdict(set)
        listOfEmptySpaces=[]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    listOfEmptySpaces.append((i,j))
                    continue
                if board[i][j] not  in setOfDigitsInRow[i]:
                    setOfDigitsInRow[i].add(board[i][j])
                else:
                    return False
                if  board[i][j] not  in setOfDigitsInCol[j]:
                    setOfDigitsInCol[j].add(board[i][j])
                else:
                    return False
                if  board[i][j] not  in setOfDigitsInBox[findTheBox(i,j)]:
                    setOfDigitsInBox[findTheBox(i,j)].add(board[i][j])
                else:
                    return False

        def backtrack(emptySpaceIndex):
            if emptySpaceIndex==len(listOfEmptySpaces):
                return True

            x,y = listOfEmptySpaces[emptySpaceIndex]
            for candidateDigit in '123456789':
                if candidateDigit not in setOfDigitsInRow[x] and candidateDigit not in setOfDigitsInCol[y] and candidateDigit not in setOfDigitsInBox[findTheBox(x,y)]:
                    board[x][y]=candidateDigit
                    setOfDigitsInRow[x].add(candidateDigit)
                    setOfDigitsInCol[y].add(candidateDigit)
                    setOfDigitsInBox[findTheBox(x,y)].add(candidateDigit)
                    result=backtrack(emptySpaceIndex+1)
                    if result:
                        return True
                    board[x][y]='.'
                    setOfDigitsInRow[x].remove(candidateDigit)
                    setOfDigitsInCol[y].remove(candidateDigit)
                    setOfDigitsInBox[findTheBox(x,y)].remove(candidateDigit)

            return False

        return backtrack(0)