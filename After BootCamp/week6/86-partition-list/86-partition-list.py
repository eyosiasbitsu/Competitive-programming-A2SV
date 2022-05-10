# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        less = ListNode()
        grater = ListNode()
        
        cur = head
        temp2 = less
        temp3 = grater
        
        while cur:
            temp1 = cur.next
            
            if cur.val >= x:
                temp3.next = cur
                temp3 = temp3.next
                
            else:
                temp2.next = cur
                temp2 = temp2.next
            
            cur.next = None
            cur = temp1
            
        temp2.next = grater.next
        
        return less.next