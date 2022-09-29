# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        target = ListNode()
        target.next = head
        res = target
        
        while n > 0:
            node = node.next
            n -= 1
            
        while node:
            target = target.next
            node = node.next
            
        target.next = target.next.next
        return res.next
    
    
    
    
    
    
    
    