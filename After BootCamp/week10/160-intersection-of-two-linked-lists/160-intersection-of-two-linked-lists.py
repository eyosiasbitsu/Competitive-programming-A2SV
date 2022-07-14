# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ta = headA
        tb = headB
        
        while ta != tb:
            ta = ta.next if ta else headB
            tb = tb.next if tb else headA
        
        return ta