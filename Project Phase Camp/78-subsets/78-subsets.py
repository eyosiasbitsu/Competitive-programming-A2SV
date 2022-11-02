class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.arr = []
        self.res = []
        
        def backtrack(idx):
            if idx == len(nums):
                temp = self.arr[::]
                self.res.append(temp)
                return
            
            self.arr.append(nums[idx])
            backtrack(idx + 1)
            self.arr.pop()
            backtrack(idx + 1)
            
        backtrack(0)
        return self.res