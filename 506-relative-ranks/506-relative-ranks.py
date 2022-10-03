class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        mapScoreIndex={score[i]:i for i in range(n)}
        correspondingTitle={i:str(i) for i in range(1,n+1)}
        correspondingTitle[1]="Gold Medal"
        correspondingTitle[2]="Silver Medal"
        correspondingTitle[3]="Bronze Medal"
        score.sort(reverse=True)
        
        resultRank=[0]*n
        for i in range(n):
            resultRank[mapScoreIndex[score[i]]]=correspondingTitle[i+1]
        
        return resultRank
        