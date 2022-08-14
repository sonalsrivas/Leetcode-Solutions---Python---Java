class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n=len(equations)
        adjList=defaultdict(list)
        for uv,val in zip(equations, values):
            u,v=uv
            adjList[v].append((u,val))
            adjList[u].append((v,1/val))
        
        res=[]
        for x,y in queries:
            if x not in adjList or y not in adjList:
                res.append(-1)
                continue
            
            vis={i:0 for i in adjList}
            q=deque()
            q.append((y,1))
            vis[y]=1
            endFlag=False
            while q:
                z,prod=q.popleft()
                vis[z]=1
                for neigh,neighVal in adjList[z]:
                    if neigh==x:
                        res.append(prod*neighVal)
                        endFlag=True
                        break
                    elif vis[neigh]==0:
                        cur=neigh
                        q.append((neigh,prod*neighVal))
                if endFlag:
                    break
            #print(x,y,cur,z)
            if y!=z and not endFlag:
                res.append(-1)
        return res