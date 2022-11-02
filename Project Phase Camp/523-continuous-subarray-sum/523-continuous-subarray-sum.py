class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        dict1 = { 0:-1 }
        temp = 0
        
        for i, v in enumerate(nums):
            temp += v
            if temp % k in dict1:
                if i - dict1[temp % k] >= 2:
                    return True
            
            else:
                dict1[temp%k] = i
        
        return False