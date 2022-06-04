class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        
        row = set()
        col = set()
        posD = set()
        negD = set()
        
        res = []
        
        def backtrack(i):
            if i == n:
                copy = ["".join(board[r]) for r in range(n)]
                res.append(copy)
                return
            
            for c in range(n):
                if (c in col or i - c in negD or
                    i + c in posD):
                    continue
                    
                col.add(c)
                posD.add(i+c)
                negD.add(i-c)
                board[i][c] = "Q"
                
                backtrack(i+1)
                
                col.remove(c)
                posD.remove(i+c)
                negD.remove(i-c)
                board[i][c] = "."
        
        backtrack(0)
        
        return res
                
                
                