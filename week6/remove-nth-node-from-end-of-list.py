# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        prev = head
        idx = l - n
        if idx == 0:
            return head.next
        for i in range(idx-1):
            prev = prev.next
        print(prev.val)
        prev.next = prev.next.next
        return head