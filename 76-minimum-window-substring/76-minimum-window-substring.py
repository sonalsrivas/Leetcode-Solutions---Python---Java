from collections import defaultdict, Counter

class Solution:
    def minWindow(self, str,arr):
        def findEnd(end):
            while end<n:
                if str[end] in setArr:
                    mapReqCharFreq[str[end]]+=1
                end+=1
                if not any(setArr[key]>mapReqCharFreq[key] for key in setArr):
                    return end
            return end

        def ifSubstringContainsAllReq():
            return not any(setArr[key]>mapReqCharFreq[key] for key in setArr)

        def updateResultStartEnd(start,end,resStart,resEnd):
            if not any(setArr[key]>mapReqCharFreq[key] for key in setArr):
                curSubstringLen=end-start
                if resEnd-resStart>curSubstringLen:
                    return start, end
            return resStart, resEnd

        def removeRedundantStartCharsInResult(start, str):
            while start<n and (str[start] not in mapReqCharFreq or mapReqCharFreq[str[start]]>setArr[str[start]]):
                if str[start] in setArr:
                    mapReqCharFreq[str[start]]-=1
                start+=1
            return start

        n=len(str)
        setArr=Counter(arr)
        resStart, resEnd=0, float('inf')
        start,end=0,0
        mapReqCharFreq = defaultdict(int)
        
        while start<n and end<n :
            if str[start] in setArr:
                end = findEnd(end)
                start = removeRedundantStartCharsInResult(start, str)
                resStart, resEnd = updateResultStartEnd(start,end,resStart,resEnd)
                
                prevStart=start
                setArr[str[start]]-=1
                start = removeRedundantStartCharsInResult(start, str)
                setArr[str[prevStart]]+=1
                
            else:
                start+=1

        return str[resStart: resEnd] if resEnd<float('inf') else ""
