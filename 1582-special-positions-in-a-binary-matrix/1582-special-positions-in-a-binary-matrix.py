class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        setOfRowsThatHaveSingle1=set()
        for row in range(m):
            countOf1s=0
            for col in range(n):
                if mat[row][col]==1:
                    countOf1s+=1
                if countOf1s>1:
                    break
            if countOf1s==1:
                setOfRowsThatHaveSingle1.add(row)
        
        noOfSpecialPositionsInMat=0
        setOfColsThatHaveSingle1=set()
        for col in range(n):
            countOf1s=0
            rowWith1=None
            for row in range(m):
                if mat[row][col]==1:
                    rowWith1=row
                    countOf1s+=1
                if countOf1s>1:
                    break
            if countOf1s==1 and rowWith1 in setOfRowsThatHaveSingle1:
                noOfSpecialPositionsInMat+=1
        return noOfSpecialPositionsInMat
        
'''

look at each row and record if it has a single 1
look at each col and record if it has a single 1

'''