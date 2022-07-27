from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea = float('inf')
        pointsSet = set()
        #xAligned = defaultdict(set)  # x coordinate : points on this axis point
        #yAligned = defaultdict(set)  # y coordinate : points on this axis point
        for x, y in points:
            pointsSet.add((x, y))
            #xAligned[x].add((x, y))
            #yAligned[y].add((x, y))
        while pointsSet:
            #for x, y in points:
            x,y = pointsSet.pop()
            for dx, dy in pointsSet:
                if (x == dx or y == dy):
                    continue
                if (x, dy) in pointsSet and (dx, y) in pointsSet:
                    area = abs(x - dx) * abs(y - dy)
                    minArea = min(minArea, area)
            
        return minArea if minArea < float('inf') else 0
