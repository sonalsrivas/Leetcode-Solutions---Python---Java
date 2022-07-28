class Solution:
    def maxIncreaseKeepingSkyline(self, a: List[List[int]]) -> int:
        n=len(a)
        maxHeightsRow=[0]*n
        maxHeightsCol=[0]*n
        IncreaseHeightLimit=0
        for i in range(n):
            for j in range(n):
                maxHeightsRow[i]=max(maxHeightsRow[i], a[i][j])
        for j in range(n):
            for i in range(n):
                maxHeightsCol[j]=max(maxHeightsCol[j], a[i][j])
            for i in range(n):
                IncreaseHeightLimit+=min(maxHeightsRow[i], maxHeightsCol[j])-a[i][j]
        return IncreaseHeightLimit