class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        r,c = 0,0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    r,c = i,j
                    break
        print(r,c)
        count = 0
        
        for i in range(r,len(board)):
            if i >= len(board):
                break
            if board[i][c] == "B":
                break
            if board[i][c] == "p":
                count += 1
                print(count)
                break
        
        for i in range(r,-1,-1):
            if i < 0:
                break
            if board[i][c] == "B":
                break
            if board[i][c] == "p":
                count += 1
                break
        
        for i in range(c,len(board[0])):
            if i >= len(board[0]):
                break
            if board[r][i] == "B":
                break
            if board[r][i] == "p":
                count += 1
                break
        
        for i in range(c,-1,-1):
            if i < 0:
                break
            if board[r][i] == "B":
                break
            if board[r][i] == "p":
                count += 1
                break
        
        return count