# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        a=[[-1 for _ in range(n)] for __ in range(m)]
        
        def fillLayer(x,y, head,a):
            i=x
            # first row from left to right
            for j in range(y, n-y):
                a[i][j]=head.val
                head=head.next
                if not head:
                    return head
            
            j=n-y-1
            # last col from up to down
            for i in range(x+1,m-x):
                a[i][j]=head.val
                head=head.next
                if not head:
                    return head
                
            i=m-x-1
            # last row from right to left
            for j in range(n-y-2, y-1,-1):
                a[i][j]=head.val
                head=head.next
                if not head:
                    return head
            
            j=y
            # first col from down to up
            for i in range(m-x-2, x,-1):
                a[i][j]=head.val
                head=head.next
                if not head:
                    return head
            return head
        
        layerNo=0
        while head :
            head=fillLayer(layerNo,layerNo, head,a)
            layerNo+=1
            
        return a