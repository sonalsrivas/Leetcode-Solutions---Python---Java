from collections import defaultdict


class Solution:
    def getAncestors(self, n, edges):
        def helper(node):
            temp = []
            if not reversedAdjacencyList[node]:
                return temp
            for directAnces in reversedAdjacencyList[node]:
                if not ancestors[directAnces]:
                    ancestors[directAnces] = helper(directAnces)
                temp.extend(ancestors[directAnces])
                temp.append(directAnces)
            temp = sorted(list(set(temp)))
            return temp

        reversedAdjacencyList = defaultdict(list)
        for u, v in edges:
            reversedAdjacencyList[v].append(u)
        ancestors = [None for _ in range(n)]
        for i in range(n):
            if not ancestors[i]:
                ancestors[i] = helper(i)
        return ancestors