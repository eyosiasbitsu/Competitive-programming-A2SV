# Definition for singly-linked list.
class head:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__ (self,val = 0):
        self.val = val
        self.next = None
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        def num(l: Optional[ListNode])-> int:
            el = []
            while l:
                el.append(l.val)
                l = l.next
            val1 = 0
            el = el[::-1]
            for num in el:
                val1 = val1*10 + num
            return val1
        num2 = num(l1)
        num3 = num(l2)
        num4 = num2 + num3
        temp = list(str(num4))
        for i in range(len(temp)-1,-1,-1):
            temp[i] = int(temp[i])
        temp = temp[::-1]
        start = head()
        
        final = start
        for i in range(len(temp)-1):
            start.val = temp[i]
            print(start.val)
            start.next = head()
            start = start.next
        start.val = temp[-1]
        return final