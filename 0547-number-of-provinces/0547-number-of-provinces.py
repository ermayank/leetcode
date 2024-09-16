class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        visited = set()
        province = 0
        ROWS = len(isConnected)
        
        def bfs(city):
            q = collections.deque([city])
            visited.add(city)
            
            while q:
                current_city = q.popleft()
                for neighbor in range(ROWS):
                    if isConnected[current_city][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        # BFS for each city
        for city in range(ROWS):
            if city not in visited:
                bfs(city)
                province += 1
        
        return province
                    
        
        