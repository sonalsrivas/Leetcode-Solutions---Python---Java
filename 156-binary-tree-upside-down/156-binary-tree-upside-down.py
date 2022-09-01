# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root, nRl=None, nRr=None):
        if not root:
            return
        
        def helper(root, rootLeft, rootRight):
            if not rootLeft:
                return root
            rootLeftLeft, rootLeftRight = rootLeft.left, rootLeft.right
            rootLeft.left=rootRight
            rootLeft.right=root
            return helper(rootLeft,rootLeftLeft, rootLeftRight)
        rootLeft, rootRight= root.left, root.right
        root.left, root.right= None, None
        return helper(root, rootLeft, rootRight)