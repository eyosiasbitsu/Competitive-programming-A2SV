class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        l = 1
        r = len(nums)
        
        while l <= r:
            mid = (l + r)//2
            count = 0
            
            for n in nums:
                if n <= mid:
                    count += 1
            
            if count > mid:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return l
        