# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dict1 = {}
        dummy = ListNode()
        dummy.next = head
        temp = head
        count = 0
        length = 0
        
        dict1[-1] = dummy
        
        while temp:
            dict1[count] = temp
            count += 1
            temp = temp.next
        
        dict1[count] = temp
        
        dict1[count - n - 1].next = dict1[count - n + 1]
        
        return dummy.next
            
            
            
            
            
            
            