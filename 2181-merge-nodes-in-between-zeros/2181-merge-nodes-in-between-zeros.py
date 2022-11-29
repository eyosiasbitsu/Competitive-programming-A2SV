# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        result = dummy
        _sum = 0
        
        head = head.next
        while head:
            if head.val == 0:
                result.next = ListNode(_sum)
                result = result.next
                _sum = 0
                
            else:
                _sum += head.val
            
            head = head.next
        
        return dummy.next