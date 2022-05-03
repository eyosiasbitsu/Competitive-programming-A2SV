# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        dummy = ListNode(0,head)
        l,last = self.l(head)
        nth = self.nth(head,l-k%l)
        
        if k%l == 0:
            return head
        
        temp = nth.next
        nth.next = None
        last.next = head
        
        return temp
        
            
    
    
    def nth(self,node,n): # n = length of the list - k
        cur = node
        n -= 1
        
        while n > 0:
            cur = cur.next
            n -= 1
        return cur
        
        
    
    
    def l(self,node):
        cur = node
        i = 0
        
        while cur:
            i += 1
            prev = cur
            cur = cur.next
        
        return (i,prev)
        