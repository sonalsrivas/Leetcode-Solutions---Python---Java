class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def isLineOverlap(X,Y,P,Q):
            # we expect X>Y and P>Q
            #print(X,Y,P,Q)
            #res= (X>Y and (X>=P>=Y or P>=X>=Q)) 
            res=(X<=P<Y or P<=X<Q)
            #print("returning : ", res)
            return res
        
        
        #  [x1, y1, x2, y2], where 
        # (x1, y1) is the coordinate of its bottom-left corner
        # (x2, y2) is the coordinate of its top-right corner
        
        verticalPoints=(rec1[1],rec1[3],rec2[1],rec2[3])
        horizontalPoints=(rec1[0],rec1[2],rec2[0],rec2[2])
        
        #print(f"verticalPoints => {verticalPoints}\n horizontalPoints ]> {horizontalPoints}")
        return isLineOverlap(*verticalPoints) and isLineOverlap(*horizontalPoints)