class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        ROWS, COLS = len(maze), len(maze[0])
        moves = 1
        
        # Queue for BFS
        q = collections.deque()
        q.append((entrance[0], entrance[1]))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Mark current cell as visited 
        maze[entrance[0]][entrance[1]] = '+'
        
        # BFS
        while q:
            qLen = len(q)
            
            for i in range(qLen):
                r,c = q.popleft()
                
                # For Each Direction (Will run 4 times)
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # Condition to continue
                    if (row < 0 or col < 0 or row >= ROWS or col >= COLS or maze[row][col] == '+'):
                        continue
                    # If we reached at Exit
                    if (row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1):
                        return moves
                    maze[row][col] = '+'
                    q.append((row, col))
            
            moves += 1
        
        return -1