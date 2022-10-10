# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        length_of_head = self.length(head)
        middle = length_of_head // 2 + 1
        
        while middle != 1:
            middle -= 1
            head = head.next
        
        return head
        
    def length(self, node):
        ln = 0
        
        while node != None:
            ln += 1
            node = node.next
        
        return ln
    
    
    
    
    