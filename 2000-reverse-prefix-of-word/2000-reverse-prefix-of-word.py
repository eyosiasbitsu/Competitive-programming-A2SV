class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        str1 = list(word)
        i = 0
        j = str1.index(ch)
        
        while i <= j:
            str1[i],str1[j] = str1[j],str1[i]
            i += 1
            j -= 1
            
        return "".join(str1)