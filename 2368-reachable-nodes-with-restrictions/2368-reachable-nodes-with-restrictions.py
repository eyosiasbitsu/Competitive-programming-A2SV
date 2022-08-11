class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        restricted = set(restricted)
        
        for i in range(len(edges)):
            fr, to = edges[i]
            
            graph[fr].append(to)
            graph[to].append(fr)
        
        seen = set()
        stk = [0]
        count = 1
        
        while stk:
            cur = stk.pop()
            
            seen.add(cur)
            
            for n in graph[cur]:
                if n not in seen and n not in restricted:
                    count += 1
                    stk.append(n)
                
        return count
            
            
            
            
            
            
            
            
            
            