class Solution:
    def sortSentence(self, s: str) -> str:
        
        str3 = s.split(" ")
        finalstring = [None]*len(str3)
        for i in range(len(str3)):
            finalstring[int(str3[i][-1])-1] = str3[i]
            
        finalstring4 = ' '.join(finalstring)
        finalstring5 = re.sub(r'[0-9]+', '', finalstring4)
    
        return finalstring5
    
