class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        count1 = defaultdict(dict)
        count2 = defaultdict(int)
        
        for i in range(len(words1)):
            word = words1[i]
            for c in word:
                count1[i][c] = 1 + count1[i].get(c, 0)
            
        for i in range(len(words2)):
            temp = defaultdict(int)
            word = words2[i]
            for c in word:
                temp[c] += 1
            
            for c in temp:
                count2[c] = max(count2[c], temp[c])
        
        res = []
        
        for i in count1:
            count = count1[i]
            flag = True
            for c in count2:
                if c not in count or count[c] < count2[c]:
                    flag = False
                    break
            
            if flag: res.append(words1[i])
            
        
        return res
                    
                    
        
        
        
        
        
        
    