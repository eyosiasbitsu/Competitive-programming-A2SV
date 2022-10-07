# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        def last(node):
            
            while node.next:
                node = node.next
            
            return node
        
        def pr(par, node, n):
            
            while node and n:
                node = node.next
                par = par.next
                n -= 1
            
            return par, node
        
        dummy = ListNode()
        dummy.next = list1
        
        p1, n1 = pr(dummy, list1, a)
        p2, n2 = pr(dummy, list1, b)
        lst = last(list2)
        
        p1.next = list2
        lst.next = n2.next
        
        return dummy.next
        
        
        
        
        
        
        