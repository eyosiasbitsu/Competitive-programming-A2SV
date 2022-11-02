class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        deleted = set()
        
        def check(st, sub_st):
            i = 0
            j = 0
            
            while i < len(sub_st) and j < len(st):
                if (j not in deleted and
                    st[j] == sub_st[i]):
                    i += 1
                
                j += 1
            
            if i < len(sub_st):
                return False
            
            return True
        
        l = 0
        r = len(removable) - 1
        
        while l <= r:
            mid = (l + r)//2
            
            for i in range(l, mid + 1):
                deleted.add(removable[i])
            
            if check(s, p):
                l = mid + 1
            
            else:
                for i in range(l, mid + 1):
                    deleted.remove(removable[i])
                
                r = mid - 1
        
        return l
            
            
            
            
            
            
            
            
            
            
            
            
            
            