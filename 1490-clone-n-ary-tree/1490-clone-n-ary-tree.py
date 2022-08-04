"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
import queue
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q=queue.Queue()
        q.put(root)
        clonedNode=Node(root.val)
        clonedHead=clonedNode
        
        originalClonedMap={root:clonedNode}
        
        while not q.empty():
            node=q.get()
            
            
            clonedNode=originalClonedMap[node]
            
            for child in node.children:
                q.put(child)
                
                clonedChildNode=Node(child.val)
                originalClonedMap[child]=clonedChildNode
                
                clonedNode.children.append(clonedChildNode)
        return clonedHead