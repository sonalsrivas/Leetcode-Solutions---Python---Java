class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervalsList=[]
        for start, end in intervals:
            
            if not mergedIntervalsList:
                mergedIntervalsList.append([start, end])
                continue
            
            prevStart, prevEnd = mergedIntervalsList[-1]
            
            if prevStart <= start <= prevEnd:
                mergedIntervalsList[-1][1]=max(prevEnd, end)
            else:
                mergedIntervalsList.append([start, end])
                
        return mergedIntervalsList