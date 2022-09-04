# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dictNestedList():
    return defaultdict(list)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapVertLevelNodeVal=defaultdict(dictNestedList)
        
        def DFS(root, horizontalLevel, verticalLevel):
            if not root:
                return
            mapVertLevelNodeVal[verticalLevel][horizontalLevel].append(root.val)
            DFS(root.left, horizontalLevel+1, verticalLevel-1)
            DFS(root.right, horizontalLevel+1, verticalLevel+1)
        
        DFS(root, 0, 0)
        
        result=[]
        for i in range(min(mapVertLevelNodeVal), max(mapVertLevelNodeVal)+1):
            temp=[]
            for j in sorted(mapVertLevelNodeVal[i].keys()):
                mapVertLevelNodeVal[i][j].sort()
                temp.extend(mapVertLevelNodeVal[i][j])
            result.append(temp)
        return result