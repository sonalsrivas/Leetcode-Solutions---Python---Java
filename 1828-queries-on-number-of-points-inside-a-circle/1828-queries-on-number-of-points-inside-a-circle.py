class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result=[]
        for cx,cy, radius in queries:
            count=0
            for x,y in points:
                distanceSq=(cx-x)**2 + (cy-y)**2
                if radius*radius>=distanceSq:
                    count+=1
            result.append(count)
        return result