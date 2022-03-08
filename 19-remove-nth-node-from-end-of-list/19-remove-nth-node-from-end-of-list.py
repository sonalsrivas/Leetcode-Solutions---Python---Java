# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth=head
        last=head
        for i in range(n):
            last=last.next
        if not last:
            return head.next
        while last.next:
            last=last.next
            nth=nth.next
        nth.next=nth.next.next
        return head