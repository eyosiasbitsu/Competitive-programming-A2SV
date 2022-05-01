class Solution:
    def countVowels(self, word: str) -> int:
        count = 0 
        n = len(word)
        
        for i in range(len(word)):
            if word[i] in "aeiou":
                count += ((i+1)*(n-i))
                print(i+1,n-i,word[i])
        
        return count