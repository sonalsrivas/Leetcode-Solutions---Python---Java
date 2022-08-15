class Solution:
    def maxScore(self, a: List[int], k: int) -> int:
        maxscore=sum(a[-k:])
        sm=maxscore
        beg=-k+1
        for i in range(k):
            sm-=a[beg-1]
            sm+=a[i]
            maxscore=max(maxscore,sm)
            beg+=1
        return maxscore