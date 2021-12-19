class MyStack:

    def __init__(self):
        self.stack = []
        self.lenstack = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.lenstack += 1

    def pop(self) -> int:
        self.lenstack -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if self.lenstack == 0:
            return True
        else:
            return False
