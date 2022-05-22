class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
        
        n = len(nums)//2
        
        for num in count:
            if count[num] == n:
                return num
        
        return -1