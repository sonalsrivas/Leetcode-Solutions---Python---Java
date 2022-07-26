class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n=len(timePoints)
        for i in range(n):
            time=timePoints[i]
            hour, minute= map(int, time.split(':'))
            timePoints[i]=hour*60+minute
            
        timePoints.sort()
        print(timePoints)
        minDifference=float('inf')
        for i in range(1,n):
            minDifference=min(minDifference, (timePoints[i]-timePoints[i-1]))
        maxMinutes = 24*60
        minDifference =min (minDifference, maxMinutes - timePoints[-1]+timePoints[0])
        return minDifference