class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        double_ended_queue = deque([i + 1 for i in range(m)])
        result = []
        
        for query in queries:
            result.append(double_ended_queue.index(query))
            del double_ended_queue[result[-1]]
            
            double_ended_queue.appendleft(query)
        
        return result
        