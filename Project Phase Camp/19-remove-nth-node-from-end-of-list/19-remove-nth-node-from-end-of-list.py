# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(head)
        dummy.next = head
        temp = dummy
        
        while n and head:
            head = head.next
            n -= 1
        
        while head:
            head = head.next
            temp = temp.next
        
        if temp.next:
            temp.next = temp.next.next
        
        return dummy.next