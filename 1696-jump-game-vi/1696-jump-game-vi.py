class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        heap = [(-nums[0],0)]
        print(len(nums))
        for i in range(1,len(nums)):
            
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            
            max_so_far = heap[0][0] - nums[i]
            heapq.heappush(heap, (heap[0][0] - nums[i],i))
            nums[i] = -max_so_far
            
        return nums[-1]