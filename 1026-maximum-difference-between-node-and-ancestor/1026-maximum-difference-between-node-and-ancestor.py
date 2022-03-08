# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], mxA=-1, mnD=10**5+1) -> int:
        if not root:
            return mxA-mnD
        if root.val>mxA:
            mxA=root.val
        if root.val<mnD:
            mnD=root.val
        return max(self.maxAncestorDiff(root.left, mxA, mnD), self.maxAncestorDiff(root.right, mxA, mnD),mxA-mnD)