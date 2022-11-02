# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        
        dummy = ListNode()
        res = dummy
        
        while l1 and l2:
            temp = l1.val + l2.val + rem
            val = (temp)%10
            res.next = ListNode(val)
            rem = temp // 10
            
            res = res.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            temp = l1.val + rem
            val = (temp)%10
            res.next = ListNode(val)
            rem = temp // 10
            
            res = res.next
            l1 = l1.next
        
        while l2:
            temp = l2.val + rem
            val = (temp)%10
            res.next = ListNode(val)
            rem = temp // 10
            
            res = res.next
            l2 = l2.next
        
        if rem:
            res.next = ListNode(1)
        return dummy.next
        
        
        
        
        
        