# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def LCAnHeight(root):
            if not root:
                return None, 0
            if not root.left and not root.right:
                return root, 1
            
            leftLCA, leftHeight=LCAnHeight(root.left)
            rightLCA, rightHeight=LCAnHeight(root.right)
            
            if leftHeight==rightHeight:
                return root, leftHeight+1
            elif leftHeight>rightHeight:
                return leftLCA, leftHeight+1
            elif leftHeight<rightHeight:
                return rightLCA, rightHeight+1

        return LCAnHeight(root)[0]
            