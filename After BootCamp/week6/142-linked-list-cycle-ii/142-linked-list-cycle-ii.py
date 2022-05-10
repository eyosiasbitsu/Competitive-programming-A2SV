# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return 
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast.next or not fast.next.next: return
        
        slow = head
        
        while slow.next:
            if slow == fast:
                return slow
            fast = fast.next
            slow = slow.next