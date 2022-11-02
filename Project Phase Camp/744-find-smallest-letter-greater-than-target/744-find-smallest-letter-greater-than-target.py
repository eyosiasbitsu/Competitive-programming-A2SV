class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        r = len(letters) - 1
        
        while r >= 0 and letters[r] > target:
            r -= 1
            
        return letters[r + 1] if r != len(letters) - 1 else letters[0]