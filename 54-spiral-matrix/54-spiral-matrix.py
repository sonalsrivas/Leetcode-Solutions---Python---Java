class Solution:
    def spiralOrder(self, inputMatrix: List[List[int]]) -> List[int]:
        resultList=[]
        noOfRows , noOfCols = len(inputMatrix), len(inputMatrix[0])

        if noOfRows==1:
            return inputMatrix[0]

        noOfLayers = int(math.ceil(min(noOfRows , noOfCols) / 2.0) )

        def traverseRowInMatrix (i, start_j, end_j, step_j):
            for j in range(start_j, end_j, step_j):
                if inputMatrix[i][j]==None:
                    continue
                resultList.append(inputMatrix[i][j])
                inputMatrix[i][j]=None
            
        def traverseColumnInMatrix (j, start_i, end_i, step_i):
            for i in range(start_i, end_i, step_i):
                if inputMatrix[i][j]==None:
                    continue
                resultList.append(inputMatrix[i][j])
                inputMatrix[i][j]=None
            
        for layer in range(noOfLayers):

            first_row = layer
            last_col = noOfCols - 1 - layer
            last_row = noOfRows - 1 - layer
            first_col = layer

            


            traverseRowInMatrix(first_row, first_col, max(first_col+1, last_col),
                                1)
            traverseColumnInMatrix(last_col, first_row, max(first_row+1, last_row),
                                   1)
            traverseRowInMatrix(last_row, last_col, min(last_col-2, first_col),
                                -1)
            traverseColumnInMatrix(first_col, last_row, min(last_row-2, first_row),
                                   -1)
        return resultList