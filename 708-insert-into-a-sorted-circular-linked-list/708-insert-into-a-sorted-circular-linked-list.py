"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode=Node(insertVal)
        if not head:
            newNode.next=newNode
            return newNode
        node=head
        #prev=None
        if node==node.next:
            node.next=newNode
            newNode.next=node
            return head
        while node:
            if node.val<=insertVal<=node.next.val or (node.val>node.next.val and (node.val<=insertVal or node.next.val>=insertVal)):
                nodeNext=node.next
                node.next=newNode
                newNode.next=nodeNext
                print(insertVal,"zaear")
                break
            node=node.next
            if node==head:
                nodeNext=node.next
                node.next=newNode
                newNode.next=nodeNext
                print(insertVal,"wsdf")
                break
            
        
        return head
                