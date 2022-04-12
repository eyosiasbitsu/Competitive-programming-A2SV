class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        drn = [(1,1),(-1,0),(0,-1),(0,1),(1,0),(1,-1),(-1,1),(-1,-1)]
        l = len(board)
        r = len(board[0])
        changed = []
        for i in range(l):
            for j in range(r):
                count = 0
                for j_add,i_add in drn:
                    new_j = j + j_add
                    new_i = i + i_add
                    if 0 <= new_i < l and 0 <= new_j < r and board[new_i][new_j] == 1:
                        count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    changed.append((i,j,0))
                elif board[i][j] == 0 and count == 3:
                    changed.append((i,j,1))
        for i,j,k in changed:
            board[i][j] = k
                