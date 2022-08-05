class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        if self.stk2:
            return self.stk2.pop()
        
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        
        return self.stk2.pop()

    def peek(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        
        return self.stk2[-1]
    def empty(self) -> bool:
        return not (self.stk1 or self.stk2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()