class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #total no. of rows in the matrix
        cols =  len(matrix[0]) #total no. of columns in the matrix
        
        row = rows - 1 #start from third corner like in ex. 1 element 18
        col = 0

        while row >= 0 and col < cols:

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        
        return False 