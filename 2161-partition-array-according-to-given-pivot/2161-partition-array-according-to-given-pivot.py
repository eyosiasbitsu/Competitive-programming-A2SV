class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        equal = []
        
        for n in nums:
            if n > pivot:
                greater.append(n)
            
            elif n < pivot:
                less.append(n)
            
            else:
                equal.append(n)
        
        return less + equal + greater