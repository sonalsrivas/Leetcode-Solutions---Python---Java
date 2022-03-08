# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        Enth=h
        last=h
        for i in range(k):
            Bnth=last
            last=last.next
        if not last:
            Enth.val,Bnth.val=Bnth.val,Enth.val
            return h
        while last:
            Enth=Enth.next
            last=last.next
        
        Enth.val,Bnth.val=Bnth.val,Enth.val
        return h