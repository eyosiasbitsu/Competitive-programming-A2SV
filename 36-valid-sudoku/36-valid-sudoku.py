class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                if ((board[r][c] in rows[r]) or 
                    (board[r][c] in cols[c]) or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                
                val = board[r][c]
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3,c//3)].add(val)
        
        return True