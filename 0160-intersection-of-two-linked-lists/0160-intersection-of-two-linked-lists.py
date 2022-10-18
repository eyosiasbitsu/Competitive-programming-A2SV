# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodeA, nodeB = headA, headB
        
        while nodeA != nodeB:
            if not nodeB:
                nodeB = headA
            
            else:
                nodeB = nodeB.next
                
            if not nodeA:
                nodeA = headB
            
            else:
                nodeA = nodeA.next
                
        return nodeA
    