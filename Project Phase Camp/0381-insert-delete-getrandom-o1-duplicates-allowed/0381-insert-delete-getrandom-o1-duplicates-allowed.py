class RandomizedCollection:

    def __init__(self):
        self.indices = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        temp = not self.indices[val]
        
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        
        return temp
        
    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        
        if self.nums[-1] == val:
            self.indices[val].remove(len(self.nums) - 1)
            self.nums.pop()
        
        else:
            index = self.indices[val].pop()
            
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.nums.pop()
            
            index_to_remove = len(self.nums)
            self.indices[self.nums[index]].remove(index_to_remove)
            
            self.indices[self.nums[index]].add(index)
        
        return True
    
    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums) - 1)
        
        return self.nums[index]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()