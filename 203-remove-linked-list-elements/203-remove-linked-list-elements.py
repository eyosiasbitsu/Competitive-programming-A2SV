# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        ar = self.arr(head,val)
        temp = dummy
        
        while temp:
            if temp not in ar:
                par = temp
                temp = temp.next
            else:
                par.next = temp.next
                temp = par.next
        
        return dummy.next
        
    def arr(self,node,tar):
        arr = set()
        temp = node
        
        while temp:
            if temp.val == tar:
                arr.add(temp)
                
            temp = temp.next
        
        return arr