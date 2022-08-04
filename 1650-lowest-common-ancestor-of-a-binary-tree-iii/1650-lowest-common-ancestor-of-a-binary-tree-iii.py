"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pAncestorMap=set([p])
        qAncestorMap=set([q])
        
        while True:
            
            if p in qAncestorMap:# or q in pAncestorMap:
                return p
            if q in pAncestorMap:
                return q
            if p:
                p=p.parent
                pAncestorMap.add(p)
            if q:
                q=q.parent
                qAncestorMap.add(q)

        return