class MyCircularDeque:
    
    def __init__(self, k: int):
        self.deque = {}
        self.length = k
        self.f = -1
        self.r = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.f == -1:
            self.r = 0
            self.f = 0
            self.deque[0] = value
            return True
        
        if self.f == 0:
            self.f = self.length - 1
            self.deque[self.f] = value
            
        else:
            self.f -= 1
            self.deque[self.f] = value
        
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.r == -1:
            self.r = 0
            self.f = 0
            self.deque[0] = value
            
            return True
        if self.r == self.length - 1:
            self.r = 0
        
        else:
            self.r += 1
        
        self.deque[self.r] = value
        
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.f == self.r:
            del self.deque[self.f]
            self.f = -1
            self.r = -1
            return True
        print(self.deque, self.f, self.r)
        del self.deque[self.f]
        
        if self.f == self.length - 1:
            self.f = 0
        
        else:
            self.f += 1
        
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.f == self.r:
            del self.deque[self.f]
            self.r = -1
            self.f = -1
            return True
        
        del self.deque[self.r]
        
        if self.r == 0:
            self.r = self.length - 1
        
        else:
            self.r -= 1
         
        return True
    def getFront(self) -> int:
        if self.f == -1:
            return -1
        
        return self.deque[self.f]

    def getRear(self) -> int:
        if self.r == -1:
            return -1
        
        return self.deque[self.r]

    def isEmpty(self) -> bool:
        if self.f == -1:
            return True

    def isFull(self) -> bool:
        if ((self.f == 0 and self.r == self.length - 1) or
           (self.f == self.r + 1)):
            return True
        
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()