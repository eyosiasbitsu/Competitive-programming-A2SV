class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        que = deque([("0000", 0)])
        seen = set()
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1
        
        while que:
            cur, count = que.popleft()
            arr = list(cur)
            
            if cur == target:
                return count
            
            for i in range(4):
                c = arr[i]
                
                if int(arr[i]) != 9:
                     arr[i] = str(int(c) + 1) 
                else: 
                    arr[i] = '0'
                    
                st = "".join(arr)
                
                if st not in seen and st not in deadends:
                    que.append((st, count + 1))
                    seen.add(st)
                
                if int(c) != 0:
                     arr[i] = str(int(c) - 1) 
                else: 
                    arr[i] = '9'
                    
                st = "".join(arr)
                
                if st not in seen and st not in deadends:
                    
                    que.append((st, count + 1))
                    seen.add(st)
                    
                arr[i] = c
        
        return -1
            