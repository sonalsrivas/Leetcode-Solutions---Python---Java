# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(root):#, subtreeSum, subtreeSize, count):
            if not root:
                return 0,0,0
            
            subtreeSumL, subtreeSizeL, countL=helper(root.left)
            subtreeSumR, subtreeSizeR, countR=helper(root.right)
            
            subtreeSum=root.val+subtreeSumL+subtreeSumR
            subtreeSize=1+subtreeSizeL+subtreeSizeR
            count=countL+countR
            
            average=subtreeSum//subtreeSize
            if average==root.val:
                count+=1
            return subtreeSum, subtreeSize, count
        return helper(root)[2]