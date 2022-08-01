# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return False
            doesLeftSubtreeContainOne=helper(root.left)
            if not doesLeftSubtreeContainOne:
                root.left=None
            doesRighttSubtreeContainOne=helper(root.right)
            if not doesRighttSubtreeContainOne:
                root.right=None
            return doesLeftSubtreeContainOne or doesRighttSubtreeContainOne or root.val==1
        
        if helper(root):
            return root
        return None