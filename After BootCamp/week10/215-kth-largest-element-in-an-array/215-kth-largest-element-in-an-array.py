class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k = len(nums) - k
        
        while nums and k > 0:
            heapq.heappop(nums)
            k -= 1
        
        return nums[0]