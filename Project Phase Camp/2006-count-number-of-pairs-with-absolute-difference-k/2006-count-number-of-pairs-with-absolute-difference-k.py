class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        set1 = defaultdict(int)
        count = 0
        nums.sort()
        
        for n in nums:
            if n - k in set1:
                count += set1[n - k]
            
            set1[n] += 1
        
        return count
                