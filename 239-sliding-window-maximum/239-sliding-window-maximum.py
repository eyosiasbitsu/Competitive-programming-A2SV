class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque([])
        
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
        
        ans = []
        ans.append(nums[queue[0]])
        idx = k
        
        while idx < len(nums):
            while queue and nums[queue[-1]] < nums[idx]:
                queue.pop()
            
            queue.append(idx)
            
            if queue[-1] - queue[0] + 1 > k:
                queue.popleft()
            
            ans.append(nums[queue[0]])
            idx += 1
        
        return ans
    
    
    
    
    
    
            
            
            
            
            