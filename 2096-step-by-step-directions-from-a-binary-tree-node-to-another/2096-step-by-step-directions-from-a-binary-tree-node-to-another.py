# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nodeS = None
    nodeT = None

    def getDirections(self, root, s, t):
        self.nodeS = None
        self.nodeT = None
        lca = self.findLCA(root, s, t)
        if not self.nodeS:
            self.nodeS = self.lookForNode(lca, s)
        if not self.nodeT:
            self.nodeT = self.lookForNode(lca, t)
        sPath = self.findPath(lca, self.nodeS)
        tPath = self.findPath(lca, self.nodeT)
        pathString = self.reverseDirectionVertically(sPath[1]) + tPath[1]
        return pathString

    def lookForNode(self, root, value):
        if not root:
            return None
        if root.val == value:
            return root
        l = self.lookForNode(root.left, value)
        r = self.lookForNode(root.right, value)
        return l if l else r

    def findPath(self, root, node):
        if not root or not node:
            return False, ''
        if root == node:
            return True, ''
        foundInLeft, leftPath = self.findPath(root.left, node)
        foundInRight, rightPath = self.findPath(root.right, node)
        if foundInRight:
            return foundInRight, 'R' + rightPath
        return foundInLeft, 'L' + leftPath

    def reverseDirectionVertically(self, dirs):
        return 'U' * len(dirs)

    def findLCA(self, root, s, t):
        if not root:
            return
        if root.val == s:
            self.nodeS = root
            return root

        elif root.val == t:
            self.nodeT = root
            return root

        l = self.findLCA(root.left, s, t)
        r = self.findLCA(root.right, s, t)
        if l and r:
            return root
        if not l:
            return r
        return l