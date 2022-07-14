class Solution:
    def digitCount(self, num: str) -> bool:
        count = defaultdict(int)
        
        for c in num:
            count[int(c)] += 1
        
        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False
        
        return True