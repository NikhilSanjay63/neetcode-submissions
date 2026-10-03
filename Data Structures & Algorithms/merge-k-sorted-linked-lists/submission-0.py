# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        tail = dummy

        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i,l))
        
        while heap:
            val, i, smallest = heapq.heappop(heap)
            tail.next = smallest
            tail = tail.next

            if smallest.next:
                heapq.heappush(heap,(smallest.next.val,i,smallest.next))
        
        return dummy.next