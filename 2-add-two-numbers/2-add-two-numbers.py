# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, linkedListHead1: Optional[ListNode], linkedListHead2: Optional[ListNode]) -> Optional[ListNode]:
        def updateVal(l, toAdd):
            l.val+=toAdd
            carryover=l.val//10
            l.val%=10
            return carryover
        carryOver=0
        linkedListHeadSum=linkedListHead1
        prev_linkedListHead1=None
        while linkedListHead1:
            valueToAdd=carryOver
            if linkedListHead2:
                valueToAdd+=linkedListHead2.val
            carryOver=updateVal(linkedListHead1, valueToAdd)

            prev_linkedListHead1=linkedListHead1
            linkedListHead1=linkedListHead1.next
            if linkedListHead2:
                linkedListHead2=linkedListHead2.next
            if not linkedListHead1 and linkedListHead2:
                prev_linkedListHead1.next=linkedListHead2
                linkedListHead1=linkedListHead2
                linkedListHead2=None
        if carryOver:
            prev_linkedListHead1.next=ListNode(carryOver)
        return linkedListHeadSum
        
        
            