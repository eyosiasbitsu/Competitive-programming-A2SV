class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicate = set()
        
        for number in nums:
            if number in duplicate:
                return True
            
            duplicate.add(number)
        
        return False