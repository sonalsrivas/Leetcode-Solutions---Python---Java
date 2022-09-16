class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearchCol(a,col,n,target):
            left, right=0,n-1
            while left<right:
                mid=(left+right)//2
                if a[mid][col]>=target:
                    right=mid
                elif a[mid][col]<target:
                    left=mid+1
            return left
        def binarySearchRow(a,n,target):
            left, right=0,n-1
            while left<right:
                mid=(left+right)//2
                if a[mid]>=target:
                    right=mid
                elif a[mid]<target:
                    left=mid+1
            return left
        
        noOfRows=len(matrix)
        noOfCols=len(matrix[0])
        row=binarySearchCol(matrix,-1,noOfRows,target)
        col=binarySearchRow(matrix[row],noOfCols,target)
        return matrix[row][col]==target