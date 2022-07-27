from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.xAligned = defaultdict(set)  # x coordinate : points on this axis point
        self.yAligned = defaultdict(set)  # y coordinate : points on this axis point
        self.pointsFreq = defaultdict(int)        # point : frequency

    def add(self, point):

        x, y = point
        self.pointsFreq[(x, y)]+=1
        self.xAligned[x].add((x, y))
        self.yAligned[y].add((x, y))
        
    def count(self, point):
        x, y = point
        totalCount = 0
        
        if x not in self.xAligned or y not in self.yAligned:
            return 0
        #print("pointsFreq= ",self.pointsFreq)
        #print("POINT = ",point)
        # choosing a point
        for otherPoint in self.xAligned[x]:
            if otherPoint == (x,y):
                continue

            otherX, otherY = otherPoint  # here --> otherX = x 
            diff = otherY - y
            #print("Initial: ", point, otherPoint, "diff= ", diff, "\tlooking for => ",(x + diff, otherY), (x + diff, y))
            
            if self.pointsFreq[(x + diff, otherY )] and self.pointsFreq[(x + diff, y)]:
                #print("Found other two points ", (x + diff, otherY ), (x + diff, y))
                #print("frequencies=> ", self.pointsFreq[(x, y + diff)], self.pointsFreq[(x + diff, otherY)],self.pointsFreq[(x + diff, y)])
                totalCount += (self.pointsFreq[otherPoint] * self.pointsFreq[(x + diff, otherY)] * self.pointsFreq[
                    (x + diff, y)])
                
            diff *= -1
            #print("DIffed :: ", point, otherPoint, "diff= ", diff, "\tlooking for => ",(x + diff, otherY), (x + diff, y))
            if self.pointsFreq[(x + diff, otherY)] and self.pointsFreq[(x + diff, y)]:
                #print("Found other two points ", (x + diff, otherY), (x + diff, y))
                #print("frequencies=> ", self.pointsFreq[otherPoint],self.pointsFreq[(x + diff, otherY )], self.pointsFreq[(x + diff, y)])
                totalCount += (self.pointsFreq[otherPoint] * self.pointsFreq[(x + diff, otherY )] *
                               self.pointsFreq[(x + diff, y)])
        #print("totalCount ",totalCount,"------------------\n")
        return totalCount