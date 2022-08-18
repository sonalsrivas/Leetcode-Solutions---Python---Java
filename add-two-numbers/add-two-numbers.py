# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def updateVal(l, toAdd):
            l.val+=toAdd
            carryover=l.val//10
            l.val%=10
            return carryover
        headRes=l1
        carryover=0
        while l1 and l2:
            carryover=updateVal(l1, l2.val+carryover)
            pl=l1
            l1=l1.next
            #pl2=l2
            l2=l2.next
        if l2:
            pl.next=l2
            l1=l2
        while l1 and carryover:
            carryover=updateVal(l1,carryover)
            pl=l1
            l1=l1.next
        
        if carryover:
            pl.next=ListNode(carryover)
        return headRes
        
        
            