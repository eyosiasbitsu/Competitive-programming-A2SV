# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        
        while head:
            temp = self.nextd(head)
            if temp[1] != 0:
                prev.next = temp[0]
                head = prev.next
            else:
                prev = head
                head = temp[0]
                
        return dummy.next
    
    def nextd(self,node):
        count = 0
        while node and node.next and node.val == node.next.val:
            node = node.next
            count += 1
        return (node.next,count)
    
    
    
    
    
    
    
    