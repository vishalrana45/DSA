class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        cols = len(matrix[0])
        high = len(matrix) * cols - 1 

        while low <= high:
            mid = low + (high - low) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return False
        