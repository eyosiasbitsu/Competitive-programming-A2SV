class MyHashMap:

    def __init__(self):
        self.arr = [None for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key] if self.arr[key] or self.arr[key] == 0 else -1

    def remove(self, key: int) -> None:
        if self.arr[key]:
            self.arr[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)