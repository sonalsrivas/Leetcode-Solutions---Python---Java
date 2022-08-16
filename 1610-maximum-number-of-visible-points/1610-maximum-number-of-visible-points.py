import math
class Solution:
    def visiblePoints(self, points, Oangle, location):
        Oangle=math.radians(Oangle)
        angleList=[]
        atOrigin=0
        locx,locy=location
        for x,y in points:
            if x==locx and y==locy:
                atOrigin+=1
                continue
            diffx=x-locx
            diffy=y-locy
            angle=math.atan2(diffy,diffx)
            angleList.append(angle)
        a=sorted(angleList)
        a=a+[angle+math.pi*2 for angle in a]
        n=len(a)
        beg=0
        count=0
        for end in range(n):
            while a[end]-a[beg]>Oangle:
                beg+=1
            count=max(count, end-beg+1)
        return count+atOrigin