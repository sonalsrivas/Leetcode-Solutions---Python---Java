# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        setOfVals=set()
        def DFS(root,k):
            if not root:
                return
            if k-root.val in setOfVals:
                return True
            setOfVals.add(root.val)
            return DFS(root.left,k) or DFS(root.right,k)
        return DFS(root,k)