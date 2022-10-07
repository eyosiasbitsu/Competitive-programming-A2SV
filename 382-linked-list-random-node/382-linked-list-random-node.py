# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.rand = {}
        temp = head
        num = 0
        
        while temp:
            self.rand[num] = temp
            temp = temp.next
            num += 1
        
        self.size = num
        
    def getRandom(self) -> int:
        n = random.randint(0, self.size - 1)
        return self.rand[n].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()