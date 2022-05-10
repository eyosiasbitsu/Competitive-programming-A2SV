class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set1 = set()
        
        for n in nums:
            if n not in set1:
                set1.add(n)
            else:
                set1.remove(n)
                
        for i in set1:
            return i
                