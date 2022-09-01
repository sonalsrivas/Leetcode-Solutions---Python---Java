"""
# Definition for a Node.
"""
from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        serializedString = ''
        q = deque()
        q.append(Node("*", [root]))
        while q:
            node = q.popleft()
            for childnode in node.children:
                q.append(childnode)
                serializedString += str(childnode.val) + " "
            serializedString += '- '
        return serializedString

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return
        string = data.split(" ")
        makeNodeIndex = 0
        n = len(string)
        root = Node("*", [])
        q = deque()
        q.append(root)
        while q and makeNodeIndex < n:
            node = q.popleft()
            while string[makeNodeIndex] != "-":
                newNode = Node(int(string[makeNodeIndex]), [])
                q.append(newNode)
                node.children.append(newNode)
                makeNodeIndex += 1
            makeNodeIndex += 1
        return root.children[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
