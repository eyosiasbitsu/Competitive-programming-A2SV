class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        original_array = []
        seen = set()

        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
        
        for num in graph:
            if len(graph[num]) == 1:
                self.dfs(original_array, graph, num, seen)
                break
        
        return original_array

    def dfs(self, arr, graph, node, seen):

        arr.append(node)
        seen.add(node)

        for neighbour in graph[node]:
            if neighbour not in seen:
                self.dfs(arr, graph, neighbour, seen)
        
