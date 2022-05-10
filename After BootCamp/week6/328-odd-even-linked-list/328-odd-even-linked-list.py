# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        te = even
        to = odd
        
        k = 1
        temp = head
        
        while temp:
            t = temp.next
            
            if k%2 == 0:
                te.next = temp
                te = te.next
                te.next = None
            else:
                to.next = temp
                to = to.next
                to.next = None
                
            k += 1
            temp = t
        
        to.next = even.next
        
        return odd.next