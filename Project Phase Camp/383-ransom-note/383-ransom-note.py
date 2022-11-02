class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count1 = defaultdict(int)
        
        for c in magazine:
            count1[c] += 1
        
        for c in ransomNote:
            if not count1[c]:
                return False
            
            count1[c] -= 1
        
        return True