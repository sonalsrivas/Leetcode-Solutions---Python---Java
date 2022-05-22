# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as D
    
class Solution:
    
    def closestKValues(self, root: Optional[TreeNode], t: float, k: int) -> List[int]:
        return list(self.h(root, t,k, D([])))
    
    def h(self, root: Optional[TreeNode], t: float, k: int, d) -> List[int]:
        if not root:    return d
        
        self.h(root.left, t, k, d)
        
        if len(d)==k:
            pl=d.popleft()
            if abs(pl-t)>abs(root.val-t):
                d.append(root.val)
            else:
                d.appendleft(pl)
                return d
        else:
            d.append(root.val)
        self.h(root.right, t, k,d)
        return d