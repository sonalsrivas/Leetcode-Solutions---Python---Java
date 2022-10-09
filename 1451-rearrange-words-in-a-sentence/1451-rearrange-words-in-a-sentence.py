class Solution:
    def arrangeWords(self, text: str) -> str:
        mapLengthWord=defaultdict(list)
        wordList=text.split()
        for word in wordList:
            mapLengthWord[len(word)].append(word.lower())
        
        resultList=[]
        firstFlag=True
        for length in sorted(mapLengthWord.keys()):
            if firstFlag:
                firstFlag=False
                mapLengthWord[length][0]=mapLengthWord[length][0].capitalize()
            resultList.extend(mapLengthWord[length])
        
        return ' '.join(resultList)
        