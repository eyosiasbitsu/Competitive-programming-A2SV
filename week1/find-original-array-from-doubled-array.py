class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        changed.sort()
        answer = []
        
        if len(changed) % 2 != 0 or changed[-1]%2 !=0:
            return [] 
        
        c = Counter(changed)   
        
        for num in changed:
            if num in c and c[num] >= 1:
                c[num] -= 1 
                if (num * 2) in c and c[(num * 2)] >= 1:
                    answer.append(num)
                    c[num*2] -= 1
            
            if len(answer) == len(changed) // 2:
                return answer
        
        return []
                