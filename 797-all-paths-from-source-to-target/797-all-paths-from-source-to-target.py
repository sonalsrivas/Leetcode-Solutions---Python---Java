class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        n=len(graph)
        def DFS(node,branch):
            if node==n-1:
                res.append(branch+[node])
            for neigh in graph[node]:
                DFS(neigh, branch+[node])
        DFS(0,[])
        return res