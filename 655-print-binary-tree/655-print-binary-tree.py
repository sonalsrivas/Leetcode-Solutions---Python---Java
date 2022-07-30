# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def findHeight(root):
            if not root:
                return -1
            return 1+max(findHeight(root.left),findHeight(root.right))
        
        height=findHeight(root)
        m=height+1
        n=2**(height+1)-1
        a=[['' for i in range(n)] for _ in range(m)]
        
        # place root
        
        
        #a[0][(n-1)//2]=str(root.val)
        
        def placeNodeInA(root, x,y,h):
            if not root:
                return
            a[x][y]=str(root.val)
            #a[x+1][y-2**(h-x-1)]=
            placeNodeInA(root.left, x+1, y-2**(h-x-1),h)
            placeNodeInA(root.right, x+1, y+2**(h-x-1),h)
        placeNodeInA(root, 0, (n-1)//2,height)
        return a