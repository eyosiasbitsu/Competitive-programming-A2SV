class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        indexes = defaultdict(list)
        res = 0
        
        for i,c in enumerate(s):
            indexes[c].append(i)
        
        def bs(ar,i):
            l,r = 0,len(ar)
            
            while l < r:
                mid = (l + r)//2
                
                if i < ar[mid]:
                    r = mid
                
                else:
                    l = mid + 1
            
            return l
        
        for w in words:
            prev = -1
            found = True
            for c in w:
                temp = bs(indexes[c], prev)
                if temp == len(indexes[c]):
                    found = False
                    break
                
                else:
                    prev = indexes[c][temp]
            
            if found:
                res += 1
        
        return res