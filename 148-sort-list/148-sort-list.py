# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getmid(head)
        
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left,right)
    
    def getmid(self,node):
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self,left,right):
        node = ListNode(0)
        res = node
        while left and right:
            temp = ListNode(0)
            if left.val < right.val:
                temp.val = left.val
                left = left.next
            else:
                temp.val = right.val
                right = right.next
            node.next = temp
            node = node.next
        
        while left:
            temp = ListNode(left.val)
            left = left.next
            node.next = temp
            node = node.next
        while right:
            temp = ListNode(right.val)
            right = right.next
            node.next = temp
            node = node.next
        return res.next