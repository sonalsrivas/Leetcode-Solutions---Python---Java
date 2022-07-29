# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        result=[]
        def helper(root, prev, ifHead):
            if not root:
                return
            if root.val in to_delete:
                if prev:
                    if prev.left==root:
                        prev.left=None
                    if prev.right==root:
                        prev.right=None
                helper(root.left, root, True)
                helper(root.right, root, True)
            else:
                if ifHead:
                    result.append(root)
                helper(root.left, root, False)
                helper(root.right, root, False)
                
        helper(root, None, True)
        return result
    