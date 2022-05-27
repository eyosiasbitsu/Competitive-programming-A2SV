class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
        
        c = s[0]
        const = count[c]
        
        for c in count:
            if count[c] != const:
                return False
        
        return True