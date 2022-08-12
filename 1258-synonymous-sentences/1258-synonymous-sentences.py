class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def backtrack(x,n,selection=[]):
            if x==n:
                yield selection
            else:
                for i in synList[x]:
                    for j in backtrack(x+1,n,selection+[i]):
                        yield j
        def find(a):
            if d[a]!=a:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        
        allsynSet=set()
        for j in synonyms:
            allsynSet=allsynSet.union(set(j))
        
        allsyn=list(allsynSet)
        #print("allsyn",allsyn)
        n=len(allsyn)
        mapAllsynSynIndex={allsyn[i]:i for i in range(n)}
        
        d=[i for i in range(n)]
        for u,v in synonyms:
            union(mapAllsynSynIndex[u],mapAllsynSynIndex[v])
        #print("d=",d)
        res=[]
        mapIndexSyn=defaultdict(list)
        for i in range(n):
            find(i)
            mapIndexSyn[d[i]].append(allsyn[i])
            #mapIndexSyn[d[i]]=sorted(mapIndexSyn[d[i]])
        #print("d=",d)
        #print("mapIndexSyn = ",mapIndexSyn)
        
        # sentence cleaning
        synList=[]
        sentence=text.split()
        
        i=0
        index=[]
        for word in sentence:
            if word in allsynSet:
                index.append(i)
                synList.append(mapIndexSyn[d[mapAllsynSynIndex[word]]])
            i+=1
        #print(synList)
        
        #print("akndjd ")
        for i in backtrack(0,len(synList)):
            #print("i= ",i)
            sent=[]
            k=0
            for j in range(len(sentence)):
                if k<len(i) and index[k]==j:
                    sent.append(i[k])
                    k+=1
                else:
                    sent.append(sentence[j])
            res.append(' '.join(sent))
        return sorted(res)