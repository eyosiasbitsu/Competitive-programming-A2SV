class MyHashSet:

    def __init__(self):
        self.arr = [None for i in range(1000001)]
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.arr[key] = None

    def contains(self, key: int) -> bool:
        return self.arr[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)