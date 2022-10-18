# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        row_direction, col_direction = 0, 1
        cur_row, cur_col = 0, -1
        
        result = [[-1 for _ in range(n)] for _ in range(m)]
        
        while head:
            next_row = cur_row + row_direction
            next_col = cur_col + col_direction
            
            if self.inbound(next_row, next_col, m, n) and \
                result[next_row][next_col] == -1:
                result[next_row][next_col] = head.val
                
                head = head.next
                cur_row = next_row
                cur_col = next_col
            
            else:
                row_direction, col_direction = col_direction, -row_direction
        
        return result
    
    def inbound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    
    
    
    
    