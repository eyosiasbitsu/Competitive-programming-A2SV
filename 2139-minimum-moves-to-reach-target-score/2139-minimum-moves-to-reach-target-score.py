class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        count = 0
        
        while target > 1:
            if target % 2 == 0:
                if not maxDoubles:
                    count += (target - 1)
                    break
                else:
                    maxDoubles -= 1
                    target //= 2
                    count += 1
            
            else:
                target -= 1
                count += 1
        
        return count