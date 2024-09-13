class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        # 2D Binary Search
        rows, cols = len(matrix), len(matrix[0])
        lRow, rRow = 0, rows-1
        
        while lRow <= rRow:
            midRow = lRow + ((rRow - lRow)//2)
            
            if matrix[midRow][0] > target:
                rRow = midRow - 1
            elif matrix[midRow][-1] < target:
                lRow = midRow + 1
            else:
                # Element row is Found
                break
        
        if not(lRow <= rRow):
            return False
        
        l,r = 0, cols-1
        row = lRow + ((rRow - lRow)//2)
        
        while l <=r:
            mid = l + ((r - l)//2)
            
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
        