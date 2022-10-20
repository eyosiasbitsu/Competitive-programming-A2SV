class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2, n - 1):
            arr = self.numberToBase(n, i)
            
            if not self.isPalindrome(arr):
                return False
        
        return True
    
    def isPalindrome(self, number_array):
        left = 0
        right = len(number_array) - 1
        
        while left < right:
            if number_array[left] != number_array[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        
    def numberToBase(self, number, base):
        if number == 0:
            return [0]
        
        digits = []
        while number:
            digits.append(int(number % base))
            number //= base
            
        return digits[::-1]