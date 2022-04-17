class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(l):
            st = l[0]
            count = 1
            
            for k in range(1,len(l)):
                if l[k] == st:
                    count += 1
                elif l[k] < st:
                    st = l[k]
                    count = 1
            return count
        
        def bs(target):
            l = 0
            r = len(words) - 1
            
            while l <= r:
                mid = (r+l)//2
                
                if words[mid] <= target:
                    l = mid + 1
                    
                elif words[mid] > target:
                    r = mid - 1
                    
                else:
                    return mid
            return l
        
        for i in range(len(queries)):
            queries[i] = f(queries[i])
        
        for i in range(len(words)):
            words[i] = f(words[i])
        
        words.sort()
        dict1 = {}
        dict1[words[-1]] = 0
        
        res = []
        # print(words,queries)
        for i in queries:
            res.append(len(words) - bs(i))
        return res
    
        
        
        
        
        