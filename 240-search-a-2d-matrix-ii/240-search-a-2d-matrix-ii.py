class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        noOfRow=len(matrix)
        if noOfRow>0:
            noOfCol=len(matrix[0])
        row=0
        col=noOfCol-1 
        while row<noOfRow and col>-1:
            if matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
            else:
                return True
        return False#matrix[row][col]==target