class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        mid_index = len(s)//2
        
        first_half = s[:mid_index]
        second_half = s[mid_index:]
        
        count_first = 0
        count_second = 0
        
        vouls = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        for c in first_half:
            if c in vouls:
                count_first += 1
        
        for c in second_half:
            if c in vouls:
                count_second += 1
        
        if count_second != count_first:
            return False
        
        return True
                