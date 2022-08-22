# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        q.append('|')
        while q:
            node=q.popleft()
            if node=='|':
                q.append('|')
                continue
            
            if node is u:
                if q and q[0]!='|': 
                    return q.popleft()
                break
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return None