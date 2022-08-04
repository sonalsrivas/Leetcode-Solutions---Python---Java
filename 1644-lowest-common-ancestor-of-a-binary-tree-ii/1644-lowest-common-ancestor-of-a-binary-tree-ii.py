# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p,q):
            
            if not root:
                return None
            if root in (p,q):
                return root
            leftLCA=helper(root.left, p,q)
            rightLCA=helper(root.right, p,q)
            if leftLCA and rightLCA:
                return root
            if leftLCA:
                return leftLCA
            return rightLCA
        
        def findInSubtree(root, target):
            if not root:
                return False
            if root==target:
                return True
            
            foundInLeftSub=findInSubtree(root.left, target)
            foundInRightSub=findInSubtree(root.right, target)
            
            return foundInLeftSub or foundInRightSub
        
        found=True
        lca=helper(root, p,q)
        if lca ==p:
            found=findInSubtree(p,q)
            
        elif lca==q:
            found=findInSubtree(q,p)
            
        return lca if found else None