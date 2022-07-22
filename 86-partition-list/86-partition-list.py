# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #   closest but less
        #   closest but greater
        less = ListNode()
        greater = ListNode()
        
        tl = less
        tg = greater
        temp = head
        
        while temp:
            if temp.val < x:
                tl.next = temp
                temp = temp.next
                tl = tl.next
                tl.next = None
            
            elif temp.val >= x:
                tg.next = temp
                temp = temp.next
                tg = tg.next
                tg.next = None
        
        tl.next = greater.next
        
        return less.next
                
                
                