class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        clr = image[sr][sc]
        
        que = deque()
        que.append((sr,sc))
        
        while que:
            i,j = que.popleft()
            image[i][j] = newColor
            
            for i_add,j_add in dirs:
                new_i,new_j = i + i_add, j + j_add
                
                if (0 <= new_i < len(image) and
                    0 <= new_j < len(image[0]) and
                    image[new_i][new_j] == clr):
                    que.append((new_i,new_j))
                    
        return image