class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        arr = []
        n,m = len(board[0]),len(board)
        set1 = set()
        
        # step 1
        for i in range(n):
            if board[0][i] == "O":
                arr.append((0,i))
                set1.add((0,i))
                
            if board[m-1][i] == "O":
                arr.append((m-1,i))
                set1.add((m-1,i))
                
        for i in range(m):
            if board[i][0] == "O":
                arr.append((i,0))
                set1.add((i,0))
                
            if board[i][n-1] == "O":
                arr.append((i,n-1))
                set1.add((i,n-1))
        
        # step2
        dr = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while arr:
            cur_i,cur_j = arr.pop()
            
            for i_add, j_add in dr:
                new_i = cur_i + i_add
                new_j = cur_j + j_add
                
                if (0 <= new_i < m and
                    0 <= new_j < n and
                    (new_i, new_j) not in set1 and
                    board[new_i][new_j] == "O"):
                    set1.add((new_i,new_j))
                    arr.append((new_i,new_j))
        
        # flip all the cells that i can flip
        
        for i in range(m):
            for j in range(n):
                if (board[i][j] == "O" and
                    (i,j) not in set1):
                    # flip
                    
                    board[i][j] = "X"
        
        
        # 1: find all the cells that are at the boundary and have value "O"
        # and add them to the set hence mark them as the ones we can't flip
        
        # 2: do dfs to find all the internal cells with value "O" and add them to the set
        
        # 3: traverse trough the matrix and flip the value of all the cells with value "O"
         # and don't exist in the set
            
        
            