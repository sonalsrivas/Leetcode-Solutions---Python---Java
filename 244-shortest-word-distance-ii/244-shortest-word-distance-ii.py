class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dictW=defaultdict(list)#{wordsDict[i]:i for i in range(len(wordsDict))}
        for i in range(len(wordsDict)):
            self.dictW[wordsDict[i]].append(i)
    def shortest(self, word1: str, word2: str) -> int:
        Dw1=self.dictW[word1]
        Dw2=self.dictW[word2]
        p=0; q=0; mdiff=abs(Dw1[p]-Dw2[q])
        while p<len(self.dictW[word1]) and q<len(self.dictW[word2]):
            mdiff=min(mdiff, abs(Dw1[p]-Dw2[q]))
            if Dw1[p]<Dw2[q]:
                p+=1
            else:
                q+=1
        return mdiff
            

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)