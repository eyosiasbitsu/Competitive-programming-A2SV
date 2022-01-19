class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList: 
    def __init__(self):
        self.size = 0
        self.head = Node(0)
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for i in range(index + 1):
            temp = temp.next
        if temp:
            return temp.val
        else:
            return -1 
        
    def addAtHead(self, val: int) -> None:
        
        self.addAtIndex(0,val)
         
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        self.size += 1
        prev = self.head
        for i in range(index):
            prev = prev.next
        to_insert = Node(val)
        to_insert.next = prev.next
        prev.next = to_insert
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        prev = self.head
        for i in range(index):
            prev = prev.next
        temp = prev.next.next
        prev.next = temp

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)