# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete, prev=None, ifRootIsHead=True):
        
        result=[]
        if not root:
            return result
        if root.val in to_delete:
            if prev:
                if prev.left==root:
                    prev.left=None
                elif prev.right==root:
                    prev.right=None
            return self.delNodes(root.left, to_delete, root, True) + self.delNodes(root.right, to_delete, root, True)
        
        if ifRootIsHead:
            result.append(root)
            
        return result+self.delNodes(root.left, to_delete, root, False) + self.delNodes(root.right, to_delete, root, False)
    