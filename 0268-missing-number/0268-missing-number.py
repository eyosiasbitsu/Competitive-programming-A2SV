class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        _xor = 0
        for n in nums:
            _xor ^= n
        
        for i in range(len(nums) + 1):
            _xor ^= i
        
        return _xor