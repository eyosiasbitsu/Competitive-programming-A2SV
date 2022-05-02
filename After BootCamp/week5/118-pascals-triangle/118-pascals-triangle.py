class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        arr = [1,1]
        
        for i in range(numRows-2):
            temp = []
            temp.append(arr[0])
            for i in range(1,len(arr)):
                temp.append(arr[i-1] + arr[i])
            temp.append(arr[-1])
            arr = temp
            ans.append(arr)
            
        return ans