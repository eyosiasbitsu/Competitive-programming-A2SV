class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        _min = float("inf")
        result = -1

        for n in nums:
            if n != _min:
                result = max(result, n - _min)
                
            _min = min(n, _min)
        
        return result
