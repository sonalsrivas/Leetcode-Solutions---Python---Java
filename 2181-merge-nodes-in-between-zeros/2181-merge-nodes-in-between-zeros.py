# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        originalHead=head
        headZero=None
        prevZeroHead=None
        while head:
            if head.val==0:
                prevZeroHead=headZero
                headZero=head
                head=head.next
                mergeSum=0
                while head and head.val!=0:
                    mergeSum+=head.val
                    prev=head
                    head=head.next
                    
                headZero.val=mergeSum
                headZero.next=head
            
        prevZeroHead.next=None
        return originalHead