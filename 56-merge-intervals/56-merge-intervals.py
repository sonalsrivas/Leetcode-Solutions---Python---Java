class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervalsList=[]
        prevStart, prevEnd=-1,-1
        for start, end in intervals:
            if prevStart <= start <= prevEnd:
                prevEnd = max(prevEnd, end)
                mergedIntervalsList[-1][1] = prevEnd
            else:
                mergedIntervalsList.append([start, end])
                prevStart, prevEnd = start, end
        return mergedIntervalsList