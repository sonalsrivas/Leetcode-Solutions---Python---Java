# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def LCAofTwoNodes(root,a,b):
            
            if not root:
                return None
            
            if root in (a,b):
                return root
            
            leftLCA=LCAofTwoNodes(root.left,a,b)
            rightLCA=LCAofTwoNodes(root.right,a,b)
            
            if leftLCA and rightLCA:
                return root
            if rightLCA:
                return rightLCA
            return leftLCA
        
        a=nodes[0]
        for i in range(1,len(nodes)):
            b=nodes[i]
            a=LCAofTwoNodes(root,a,b)
        return a