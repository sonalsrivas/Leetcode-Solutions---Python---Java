class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def isLineOverlap(X,Y,P,Q):
            return X<=P<Y or P<=X<Q
        
        verticalPoints=(rec1[1],rec1[3],rec2[1],rec2[3])
        horizontalPoints=(rec1[0],rec1[2],rec2[0],rec2[2])
        
        return isLineOverlap(*verticalPoints) and isLineOverlap(*horizontalPoints)