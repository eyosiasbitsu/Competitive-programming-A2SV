class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming = defaultdict(set)
        
        for i in range(len(graph)):
            for j in graph[i]:
                incoming[j].add(i)
                
        outgoing = [0]*len(graph)
        for i in range(len(graph)):
            outgoing[i] = len(graph[i])
        
        no_out = deque()
        
        for i in range(len(outgoing)):
            if outgoing[i] == 0:
                no_out.append(i)
        ans = []
        while no_out:
            temp = no_out.popleft()
            ans.append(temp)
            for j in incoming[temp]:
                outgoing[j] -= 1
                if outgoing[j] == 0:
                    no_out.append(j)
        ans.sort()
        return ans
                
        
        
        
        