class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]*(len(nums) + 1)
        post = [0]*(len(nums) + 1)
        
        i = 0
        j = len(nums) - 1
        
        while i < len(nums) and j >= 0:
            if i == 0 and j == len(nums) - 1:
                pre[i] = nums[i]
                post[j] = nums[j]
                i += 1
                j -= 1
                
            else:
                pre[i] = pre[i-1] + nums[i]
                post[j] = post[j + 1] + nums[j]
                i += 1
                j -= 1
                
        for i in range(len(nums)):
            if pre[i-1] == post[i+1]:
                return i
            
        return -1