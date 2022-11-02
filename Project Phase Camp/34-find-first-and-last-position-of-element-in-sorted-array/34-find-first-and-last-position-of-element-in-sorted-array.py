class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        low = -1
        high = -1
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r)//2
            if nums[mid] >= target:
                r = mid - 1
            
            else:
                l = mid + 1
                
        if l < len(nums) and nums[l] == target:
            low = l
            
        if low >= 0:
            r = len(nums) - 1
            
            while l <= r:
                mid = (l + r)//2

                if nums[mid] > target:
                    r = mid - 1

                else:
                    l = mid + 1
                    
            if r >= 0 and nums[r] == target:
                high = r
        
        return [low, high]