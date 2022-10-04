# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        mapNTrees={i:[] for i in range(n+1)}
        mapNTrees[0].append(None)
        mapNTrees[1].append(TreeNode())
        
        resultList=[]
        for i in range(3,n+1):
            
            remaining_i=i-1
            if remaining_i%2==1:  # only move ahead with tree making when the remaining nodes is even
                continue
            for leftChildNodes in range(1,remaining_i+1,2):
                rightChildNodes = remaining_i - leftChildNodes
                for leftSubtree in mapNTrees[leftChildNodes]:
                    
                    for rightSubtree in mapNTrees[rightChildNodes]:
                        root=TreeNode()
                        root.left=leftSubtree
                        root.right=rightSubtree
                        mapNTrees[i].append(root)
                        
        return mapNTrees[n]