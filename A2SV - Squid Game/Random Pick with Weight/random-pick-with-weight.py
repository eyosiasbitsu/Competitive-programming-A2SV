class Solution:
    
    def __init__(self, w: List[int]):
        self.w = []
        temp_total = 0

        for i in range(len(w)):
            temp_total += w[i]
            self.w.append(temp_total)
        
        self.total = temp_total

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)

        for i in range(len(self.w)):
            if self.w[i] >= rand:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
