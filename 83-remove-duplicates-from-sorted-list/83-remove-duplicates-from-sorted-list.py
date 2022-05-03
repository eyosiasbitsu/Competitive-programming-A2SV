# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = head
        temp = head.next
        
        while prev and temp:
            while temp and temp.val == prev.val:
                temp = temp.next
            
            prev.next = temp
            prev = temp
            
            if prev:
                temp = prev.next
                
        return head
            
        