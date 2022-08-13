class Solution:
    def maxPower(self, s: str) -> int:
        count=0
        i=0
        n=len(s)
        while i<n:
            curCnt=0
            curEle=s[i]
            while i<n and curEle==s[i]:
                i+=1
                curCnt+=1
            else:
                i-=1
            i+=1
            count=max(count, curCnt)
        return count