class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        arr = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i >= 1 and n == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                temp = n + nums[l] + nums[r]
                
                if temp > 0:
                    r -= 1
                
                elif temp < 0:
                    l += 1
                
                else:
                    arr.append([n, nums[l], nums[r]])
                    l += 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
        return arr
                    
                    
                    
                    
                    
                    
                    
                    
                    