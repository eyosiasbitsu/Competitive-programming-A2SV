# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        res = self.add(l1, l2)
        
        return self.reverse(res)
        
    def reverse(self, node):
        par = None
        
        while node:
            temp = node.next
            node.next = par
            
            par = node
            node = temp
        
        return par
            
    def add(self, node1, node2):
        
        rem = 0
        
        dummy = ListNode()
        res = dummy
        
        while node1 and node2:
            temp = node1.val + node2.val + rem
            val = (temp)%10
            res.next = ListNode(val)
            rem = temp // 10
            
            res = res.next
            node1 = node1.next
            node2 = node2.next
            
        while node1:
            temp = node1.val + rem
            val = (temp)%10
            res.next = ListNode(val)
            rem = temp // 10
            
            res = res.next
            node1 = node1.next
        
        while node2:
            temp = node2.val + rem
            val = (temp)%10
            res.next = ListNode(val)
            rem = temp // 10
            
            res = res.next
            node2 = node2.next
        
        if rem:
            res.next = ListNode(1)
        return dummy.next