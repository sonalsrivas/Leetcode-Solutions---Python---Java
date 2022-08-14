class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n=len(equations)
        adjList=defaultdict(list)
        for uv,val in zip(equations, values):
            u,v=uv
            adjList[v].append((u,val))
            adjList[u].append((v,1/val))
        #print(adjList)
        res=[]
        for y,x in queries:
            #print(x,y)
            if x not in adjList or y not in adjList:
                res.append(-1)
                continue
            
            vis={i:0 for i in adjList}
            q=deque()
            q.append((x,1))
            vis[x]=1
            endFlag=False
            while q:
                z,prod=q.popleft()
                #print(z,prod)
                vis[z]=1
                for neigh in adjList[z]:
                    if neigh[0]==y:
                        res.append(prod*neigh[1])
                        endFlag=True
                        break
                    elif vis[neigh[0]]==0:
                        q.append((neigh[0],prod*neigh[1]))
                if endFlag:
                    break
            if x!=z and not endFlag:
                print(x,y,z,prod)
                res.append(-1)
        return res