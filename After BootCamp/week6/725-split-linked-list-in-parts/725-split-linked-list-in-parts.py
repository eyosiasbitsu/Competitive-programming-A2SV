# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        out = []
        
        cur, l = head, self.l(head)
        lvl, rem = l//k, l%k
        prev = None
        
        for _ in range(k):
            out.append(cur)
            
            for _ in range(lvl):
                if cur:
                    prev = cur
                    cur = cur.next
            
            if rem and cur:
                prev = cur
                cur = cur.next
                rem -= 1
                
            if prev: prev.next = None
        
        return out
        
    def l(self,node):
        n = 0
        
        while node:
            n += 1
            node = node.next
        
        return n