class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a,b in connections}
        neighbours = {city:[] for city in range(n)}

        visited = set()
        changes = 0

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbours, visited, changes

            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                # neighbour reach city 0
                if (neighbour, city) not in edges:
                    changes += 1
                visited.add(neighbour)
                dfs(neighbour)
        visited.add(0)
        dfs(0)

        return changes
        