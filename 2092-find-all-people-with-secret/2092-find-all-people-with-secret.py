class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x:x[-1])
        
        meeting_dict = collections.defaultdict(list)
        
        for i in meetings:
            meeting_dict[i[-1]].append([i[0],i[1]])
            
        has_secret = {0,firstPerson}
        
        for time,meet in meeting_dict.items():
            graph = collections.defaultdict(list)
            
            seen = set()
            for p1,p2 in meet:
                graph[p1].append(p2)
                graph[p2].append(p1)
                
                if p1 in has_secret:
                    seen.add(p1)
                if p2 in has_secret:
                    seen.add(p2)
            
            que = collections.deque(seen)
            
            while que:
                cur = que.popleft()
                
                for nbr in graph[cur]:
                    if nbr not in has_secret:
                        has_secret.add(nbr)
                        
                        que.append(nbr)

                        
        return has_secret
            
            
            
            
            
            
            
            
            
            