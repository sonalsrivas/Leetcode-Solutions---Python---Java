# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def LCAnHeight(root):
            if not root:
                return None, 0
            lLCA, lhei=LCAnHeight(root.left)
            rLCA, rhei=LCAnHeight(root.right)
            if lhei>rhei:
                return lLCA, lhei+1
            elif lhei<rhei:
                return rLCA, rhei+1
            return root, lhei+1
        return LCAnHeight(root)[0]