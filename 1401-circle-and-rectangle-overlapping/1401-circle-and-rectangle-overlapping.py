class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # Bring the rectangle to the origin where the origin can then act as the cirlce (via radius reach).
        x1-=xCenter
        x2-=xCenter
        y1-=yCenter
        y2-=yCenter
        
        # Determine the point on the rectangle closest to the circle
        distanceOfClosestRectPointToCircle=0
        if x1*x2>0:
            distanceOfClosestRectPointToCircle=min(x1*x1,x2*x2)
        if y1*y2>0:
            distanceOfClosestRectPointToCircle+=min(y1*y1,y2*y2)
        
        return distanceOfClosestRectPointToCircle <= radius*radius