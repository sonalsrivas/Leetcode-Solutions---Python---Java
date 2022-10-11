# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        resultantLLHead=None
        minimumLLValueHeapList=[]
        heapq.heapify(minimumLLValueHeapList)
        k=len(lists)
        mapValueNode=defaultdict(set)
        for LinkedListIndex in range(k):
            head = lists[LinkedListIndex]
            if head:
                heapq.heappush( minimumLLValueHeapList, head.val)
                mapValueNode[head.val].add(head)
                lists[LinkedListIndex]=head.next
        previousMinimumNode=None
        while minimumLLValueHeapList:
            minimumNodeValue=heapq.heappop( minimumLLValueHeapList )
            minimumNode=mapValueNode[minimumNodeValue].pop()
            
            if not resultantLLHead:
                resultantLLHead = minimumNode
            else:
                previousMinimumNode.next=minimumNode
            
            nextNodeToMinimumNode=minimumNode.next
            if nextNodeToMinimumNode:
                heapq.heappush( minimumLLValueHeapList, nextNodeToMinimumNode.val)
                mapValueNode[nextNodeToMinimumNode.val].add(nextNodeToMinimumNode)
            previousMinimumNode=minimumNode
        
        return resultantLLHead