class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n=len(values)
        maxScore=0
        mapValsIndex={values[i]:[] for i in range(n)}
        for i in range(n):
            mapValsIndex[values[i]].append(i)
        sortedVals=sorted(values,reverse=True)
        mapChoosenLabels={i:0 for i in labels}
        print(sortedVals)
        for i in sortedVals:
            iLabel=labels[mapValsIndex[i].pop()]
            print("running for => ",i,iLabel )
            if numWanted==0:
                break
            #ogIndex=mapValsIndex[i]
            #iLabel=labels[ogIndex]
            if mapChoosenLabels[iLabel]<useLimit:
                print("CHOSE:: ", i, iLabel,maxScore)
                mapChoosenLabels[iLabel]+=1
                maxScore+=i
                numWanted-=1
            
        return maxScore