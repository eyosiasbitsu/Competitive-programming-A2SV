# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head.next:
            return True
        stk = []
        l = 0
        
        fast = head
        slow = head
        
        while fast and fast.next:
            
            stk.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            l += 2
            
        if fast:
            l += 1
            
        if l % 2 != 0:
            slow = slow.next
            
        while stk and slow:
            
            if stk[-1] != slow.val:
                return False
            
            stk.pop()
            slow = slow.next
            
        return True