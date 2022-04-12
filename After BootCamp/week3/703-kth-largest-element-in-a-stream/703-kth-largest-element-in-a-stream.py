class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        self.comp()
        
    def comp(self):
        n = 0
        self.arr2 = []
        n = self.k if self.k < len(self.arr) else len(self.arr)
        for i in range(n):
            self.arr2.append(self.arr[i])
            heapq.heapify(self.arr2)
        if(self.k == n):
            for i in range(self.k, len(self.arr)):
                if self.arr[i] > self.arr2[0]:
                    self.arr2[0] = self.arr[i]
                    heapq.heappop(self.arr2)
                    heapq.heappush(self.arr2, self.arr[i])

    def add(self, val: int) -> int:
        if len(self.arr2) < self.k:
            heapq.heappush(self.arr2, val)
        elif len(self.arr2) == self.k and val > self.arr2[0]:
            self.arr2[0] = val
            heapq.heappop(self.arr2)
            heapq.heappush(self.arr2, val)
        return self.arr2[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)