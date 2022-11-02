class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count_1_bits(n):
            count = 0
            
            num = n
            while n:
                if n & 1 == 1:
                    count += 1
                    
                n >>= 1
            
            return count
        
        arr.sort(key = lambda x : (count_1_bits(x),  x))
        
        return arr
                