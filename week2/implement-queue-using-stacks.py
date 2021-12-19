class MyQueue:

    def __init__(self):
        self.queue1 = []
        
    def push(self, x: int) -> None:
        self.queue1.append(x)
        
    def pop(self) -> int:
        return self.queue1.pop(0)
    
    def peek(self) -> int:
        return self.queue1[0]
    
    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        else:
            return False
