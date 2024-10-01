class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) mark rows and cols to be zeroed in the first row and col
        firstRow = False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Mark rows and cols to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstRow = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        #First Row
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # First Column
        if firstRow:
            for c in range(COLS):
                matrix[0][c] = 0