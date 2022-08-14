class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def find(a):
            if a!=d[a]:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        
        if len(sentence1)!=len(sentence2):
            return False
        d={}
        for u,v in similarPairs:
            if u not in d:
                d[u]=u
            if v not in d:
                d[v]=v
            union(u,v)
            
        n=len(sentence1)
        for i in range(n):
            if sentence1[i]==sentence2[i]:
                pass
            elif (sentence1[i] in d and sentence2[i] in d and find(sentence1[i])!=find(sentence2[i])) or ((sentence1[i] not in d) or (sentence2[i] not in d)):
                return False
        return True