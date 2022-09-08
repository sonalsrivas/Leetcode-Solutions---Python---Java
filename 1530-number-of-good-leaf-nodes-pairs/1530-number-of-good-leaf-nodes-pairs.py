# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.c=0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.c=0
        mapDistnumOfLeaves=defaultdict(int)
        def DFS(root):
            if not root:
                return {}
            if not root.left and not root.right:
                return {1:1}
            leftMap=DFS(root.left)
            rightMap=DFS(root.right)
            for i in leftMap:
                for j in rightMap:
                    if i+j<=distance:
                        self.c+=leftMap[i]*rightMap[j]
            mapN={i:0 for i in range(11)}
            for i in leftMap:
                if i in rightMap and i<10:
                    mapN[i+1]+=leftMap[i]+rightMap[i]
                elif i<10:
                    mapN[i+1]+=leftMap[i]
            for i in rightMap:
                if i not in leftMap and i<10:
                    mapN[i+1]+=rightMap[i]
            return mapN
            
        DFS(root)
        return self.c