# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        dm = ListNode(0,dummy)
        length = self.l(head)
        
        p0,p1,n1 = self.kth(dm,k+1)
        p2,p3,n2 = self.kth(dm,length-k+2)
        
        if p3 == n1:
            print(p0.next.val)
            p1.next = n2
            temp = n2.next
            n2.next = p3
            
            n1.next = temp
        elif p1 == n2:
            p0.next = n1
            temp = n1.next
            n1.next = n2
            
            n2.next = temp
        
        else:
            p1.next = n2
            temp = n2.next
            n2.next = n1.next

            p3.next = n1
            n1.next = temp
        
        return dummy.next
    
    
    
    def l(self,node):
        
        cur = node
        k = 0
        
        while cur:
            cur = cur.next
            k += 1
            
        return k
    
    def kth(self,node,k):
        cur = node
        prev = cur
        while k > 0:
            pr = prev
            prev = cur
            cur = cur.next
            k -= 1
        
        return (pr,prev,cur)