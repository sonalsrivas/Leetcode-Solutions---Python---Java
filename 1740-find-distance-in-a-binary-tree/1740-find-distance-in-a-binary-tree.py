# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def findLCA(root, p,q):
            if not root:
                return
            if root.val in (p,q):
                return root
            l=findLCA(root.left, p,q)
            r=findLCA(root.right, p,q)
            if l and r:
                return root
            if l:
                return l
            return r
        
        def findHeight(root, x, h=0):
            if not root:
                return 0
            if root.val==x:
                return h
            l=findHeight(root.left, x, h+1) 
            r=findHeight(root.right, x, h+1)
            if l:
                return l
            return r
        
        pHeight=findHeight(root, p)
        qHeight=findHeight(root, q)
        lcaHeight=findHeight(root, findLCA(root, p,q).val)
        return pHeight+qHeight-lcaHeight-lcaHeight