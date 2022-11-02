# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ln = -1
        temp = head
        
        while temp:
            temp = temp.next
            ln += 1
        
        res = 0
        
        while head:
            res += ((2**ln)*head.val)
            head = head.next
            ln -= 1
        
        return res