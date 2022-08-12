class Solution:
    def accountsMerge(self, a: List[List[str]]) -> List[List[str]]:
        
        def find(a):
            if d[a]!=a:
                d[a]=find(d[a])
            return d[a]
        def union(a,b):
            d[find(a)]=find(b)
        
        n=len(a)
        d=[i for i in range(n)]
        
        mapEmailIndex=defaultdict(list)
        
        for i in range(n):
            for j in range(1,len(a[i])):
                mapEmailIndex[a[i][j]].append(i)
        #making union find arrangement
        for indxList in mapEmailIndex.values():
            for j in range(1,len(indxList)):
                union(indxList[j-1],indxList[j])
        
        res=defaultdict(list)
        # collecting all common emails 
        for i in range(n):
            find(i)     # to make UF tree more direct
            temp=[]
            for j in set((d[i],i)):
                temp.extend(a[j][1:])
                res[d[i]].extend(temp)
        
        for i in res:
            res[i]=sorted(list(set(res[i])))
            res[i].insert(0,a[i][0])
        return res.values()