class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def findSmallestRegion(self, regions, region1, region2):
        def findNaryTreeLCA(root, node1, node2):
            if not root:
                return
            if root.val in (node1, node2):
                return root
            childLCAFind1 = None
            for childnode in root.children:
                childSubtreeFind = findNaryTreeLCA(childnode, node1, node2)
                if childSubtreeFind and childLCAFind1:
                    return root
                elif childSubtreeFind:
                    childLCAFind1 = childSubtreeFind
            return childLCAFind1

        allNodes = dict()
        nonHeadNodes = dict()
        for regionFamily in regions:
            parentNode = None
            for region in regionFamily:
                if region not in allNodes:
                    node = TreeNode(region)
                    allNodes[region] = node
                else:
                    node = allNodes[region]
                if not parentNode:
                    parentNode = node
                    continue
                parentNode.children.append(node)
                nonHeadNodes[region] = node
        for i in nonHeadNodes:
            allNodes.pop(i)
        root = allNodes.popitem()[1]
        return findNaryTreeLCA(root, region1, region2).val