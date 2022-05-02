# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        count = 0
        
        while temp:
            temp = temp.next
            count += 1
            if count >= 10001:
                return True
            
        return False
        