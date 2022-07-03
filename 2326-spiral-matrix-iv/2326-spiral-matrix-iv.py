# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        left_b = 0
        right_b = n - 1
        top_b = 0
        bottom_b = m - 1
        
        while head:
            i,j = top_b,left_b
            
            while j <= right_b and head:
                matrix[i][j] = head.val
                head = head.next
                j += 1
            
            top_b += 1
            j = right_b
            i = top_b
            
            while i <= bottom_b and head:
                matrix[i][j] = head.val
                head = head.next
                i += 1
            
            right_b -= 1
            i = bottom_b
            j = right_b
            
            while j >= left_b and head:
                matrix[i][j] = head.val
                head = head.next
                j -= 1
            
            bottom_b -= 1
            i = bottom_b
            j =  left_b
            
            while i >= top_b and head:
                matrix[i][j] = head.val
                head = head.next
                i -= 1
            
            left_b += 1
        
        return matrix
    
#         1 , 3 [0,1,2]
#         3, 5 [3,0,2,6,8,1,7,9,4,2,5,5,0,2,3]
#         3, 5 [3,0,2,6,8,1,7,9,4,2,5,5,0]

#         [[3, 0, 2, 6, 8],
#          [-1 (i = 1, j = 0), -1, -1, -1, -1],
#          [-1(i = 2, j = 0), -1, -1, -1, -1]]

#         creating the matrix O(m*n) time and O(m*n)
#         overall time O(m*n), overall space O(m*n)

#         left_b = 0 this will be incremented when i reach the position (top_b + 1, left_b)
#         right_b = n - 1 = 4 will be decremented wehen i reach the position (bottom_b, right_b)
#         top_b = 0 will be incemented when i reach (top_b, rightb)
#         bottom_b = m - 1 = 3 decremented when i reach (bottom_b, left_b)

#         head points to 3
#         the head is going to be changed  and its value is going to 
#         be stored in the matrix as i iterate in spiral manner
#         over the ubove matrix
        
#         at first i'm at the top left position
#         i will store the current value of the head at this position and move the head to the next
#         head points to 0
#         which cell am i supposed to go to? (0,1)
#         i will store the current value of the head at this position and move the head to the next
#         
#         
        
        
        
        
        
        
        
        
        