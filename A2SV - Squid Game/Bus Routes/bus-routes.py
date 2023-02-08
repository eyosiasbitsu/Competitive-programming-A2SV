class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        graph = defaultdict(set)
        
        for bus, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(bus)
        
        queue = deque([(source, 0)])
         
        seen_stops = set()
        seen_buses = set()
        
        while queue:
            stop, count = queue.popleft()
            if stop == target:
                    return count
                
            for bus in graph[stop]:
                if bus not in seen_buses:
                    seen_buses.add(bus)
                    
                    for stop in routes[bus]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop, count + 1))
        return -1
