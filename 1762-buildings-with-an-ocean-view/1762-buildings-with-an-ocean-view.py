class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeightYet=0
        res=[]
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>maxHeightYet:
                res.append(i)
                maxHeightYet=heights[i]
        return res[::-1]
                