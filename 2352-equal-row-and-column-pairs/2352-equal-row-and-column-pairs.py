class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Create Row Hash 
        # Create col hash
        # iterate and give result
        n = len(grid)
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        
        rowCount = {}
        
        for row in grid:
            rowStr = str(row)
            if rowStr in rowCount:
                rowCount[rowStr] += 1
            else:
                rowCount[rowStr] = 1
            
        for r in range(ROWS):
            # Get Cols
            column = []
            for c in range(COLS):
                column.append(grid[c][r])
            
            
            colStr = str(column)
            if colStr in rowCount:
                res += rowCount[colStr]
        
        return res
                

            
            
        