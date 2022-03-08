# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.maxAminD(root)
    def maxAminD(self, root, mxA=-1, mnD=10**5):
        nx=10**5
        if not root:
            return mxA-mnD
        if root.val>mxA:
            mxA=root.val
        if root.val<mnD:
            mnD=root.val
        mcandi=max(self.maxAminD(root.left, mxA, mnD), self.maxAminD(root.right, mxA, mnD))
        return max(mcandi,mxA-mnD)