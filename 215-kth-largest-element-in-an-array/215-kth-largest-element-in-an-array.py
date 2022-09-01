class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ar = [0 for _ in range(2*(10**4) + 1)]
        
        for n in nums:
            ar[n + 10**4] += 1
        
        for i in range(len(ar) - 1, -1, -1):
            if k - ar[i] <= 0:
                return i - 10**4
                
            k -= ar[i]
        