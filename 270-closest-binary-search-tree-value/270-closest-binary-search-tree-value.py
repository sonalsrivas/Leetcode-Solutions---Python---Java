# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], x: float, a=float('inf')) -> int:
        if not root:
            return a
        if abs(x-root.val)<abs(x-a):
            a=root.val
        l=self.closestValue(root.left,x,a)
        r=self.closestValue(root.right,x,a)
        b= l if abs(x-l)<abs(x-r) else r
        return b if abs(x-b)<abs(x-a) else a