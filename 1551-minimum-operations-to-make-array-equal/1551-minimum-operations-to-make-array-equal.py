class Solution:
    def minOperations(self, n: int) -> int:
        
        arr = []
        _sum = 0
        min_operations = 0
        
        for i in range(n):
            arr.append(2*i + 1)
            _sum += arr[-1]
        
        average_vaue = _sum // n
        
        for num in arr:
            if num > average_vaue:
                min_operations += (num - average_vaue)
        
        return min_operations