class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        q = collections.deque()
        q.append(0)
        
        while q:
            room = q.popleft()
           
            for i in rooms[room]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        
        return len(visited) == len(rooms)
        