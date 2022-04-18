# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        arr = [-100001]
        l1 = 0
        heapq.heapify(arr)
        for i in range(len(lists)):
            while lists[i]:
                x = lists[i].val
                heapq.heappush(arr,x)
                l1+=1
                lists[i] = lists[i].next
        head = ListNode()
        temp = head
        arr2 = []
        heapq.heappop(arr)
        for i in range(l1):
            # temp.val = ()
            temp.next = ListNode(heapq.heappop(arr))
            temp = temp.next
        res = random.sample(range(-10000, 10000), 10000)
        return head.next