class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        count = defaultdict(int)
        res = []
        
        for n in digits:
            count[n] += 1
        
        for i in range(100,999,2):
            temp = str(i)
            t_count = defaultdict(int)
            flag = True
            
            for d in temp:
                t_count[int(d)] += 1
                
            for n in t_count:
                if t_count[n] > count[n]:
                    flag = False
                    break
            
            if flag:
                res.append(i)
        
        return res
                
            