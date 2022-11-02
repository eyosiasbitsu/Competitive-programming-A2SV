# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        temp = dummy
        
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        while heap:
            val, idx = heapq.heappop(heap)
            cur = lists[idx]
            nxt = cur.next
            cur.next = None
            
            temp.next = cur
            temp = temp.next
            
            lists[idx] = nxt
            
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        
        return dummy.next