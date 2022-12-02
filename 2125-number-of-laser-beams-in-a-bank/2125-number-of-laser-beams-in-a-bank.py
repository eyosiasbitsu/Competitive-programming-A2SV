class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        prev = 0
        result = 0
        
        for i in range(len(bank)):
            cur = 0
            
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    cur += 1
            
            result += (cur*prev)
            if cur != 0:
                prev = cur
        
        return result