# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        
        n=len(nums)
        mapIntegerIndex = {nums[i]:i for i in range(n)}

        def helper(nums, start, end ):

            # should return the root of the subtree 
            if end - start < 0: # base conditions
                return None
            maxIntegerFromStartToEnd = max(nums[start: end+1])
            root = TreeNode(maxIntegerFromStartToEnd)

            currentMaxIndex = mapIntegerIndex[maxIntegerFromStartToEnd]

            leftSubtreeRoot = helper(nums, start, currentMaxIndex-1)
            rightSubtreeRoot = helper(nums, currentMaxIndex+1, end)

            root.left = leftSubtreeRoot
            root.right = rightSubtreeRoot

            return root

        return helper(nums, 0, n-1)