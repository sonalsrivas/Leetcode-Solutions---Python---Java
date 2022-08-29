# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dictVertiDist=defaultdict(list)
        q=deque()
        q.append((root, 0))
        while q:
            node, distance=q.popleft()
            dictVertiDist[distance].append(node.val)
            if node.left:
                q.append((node.left, distance-1))
            if node.right:
                q.append((node.right, distance+1))
        res=[]
        for distance in sorted(dictVertiDist.keys()):
            res.append(dictVertiDist[distance])
        return res