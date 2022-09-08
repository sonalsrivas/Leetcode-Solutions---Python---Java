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
                #mapDistnumOfLeaves[height]+=1
                return {1:1}
            leftMap=DFS(root.left)
            rightMap=DFS(root.right)
            print(root.val,leftMap,rightMap)
            for i in leftMap:
                for j in rightMap:
                    if i+j<=distance:
                        #print(self.c,leftMap[i],rightMap[j])
                        self.c+=leftMap[i]*rightMap[j]
            mapN={i:0 for i in range(11)}
            for i in leftMap:
                if i in rightMap and i<10:
                    mapN[i+1]+=leftMap[i]+rightMap[i]
                    #print("~~",i+1,mapN[i+1])
                elif i<10:
                    mapN[i+1]+=leftMap[i]
                    #print("~~",i+1,mapN[i+1])
            for i in rightMap:
                if i not in leftMap and i<10:
                    mapN[i+1]+=rightMap[i]
            #print("mapN = ",mapN)
            return mapN
            #return max(leftHeight, rightHeight)
        DFS(root)
        return self.c
        print(mapDistnumOfLeaves)
        c=0
        for i in mapDistnumOfLeaves:
            for j in mapDistnumOfLeaves:
                if i+j>distance:
                    continue
                if i==j:
                    c+=math.factorial(mapDistnumOfLeaves[i])
                else:
                    c+=mapDistnumOfLeaves[i]*mapDistnumOfLeaves[j]
        return c