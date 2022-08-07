# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTreeStructure={}
        commons=set()
        def DFShash(root):
            if not root:
                return ''
            leftHash=DFShash(root.left)
            rightHash=DFShash(root.right)
            
            if leftHash=='':
                pass
            elif leftHash not in subTreeStructure:
                subTreeStructure[leftHash]=root.left
            else:
                commons.add(leftHash)
            if rightHash=='':
                pass
            elif rightHash not in subTreeStructure:
                subTreeStructure[rightHash]=root.right
            else:
                commons.add(rightHash)
            return str(root.val)+'/'+leftHash+'/'+rightHash+'-'
            
        DFShash(root)
        res=[]
        for hash_ in commons:
            res.append(subTreeStructure[hash_])
        return res