class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mid):
            rows = len(matrix)
            cols = len(matrix[0])

            row = rows - 1 #start from any corner
            col = 0
            count = 0 #to check how many element before guess is it k or not

            while row >= 0 and col < cols:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            
            return count
        
        n = len(matrix)
        low = matrix[0][0] #smallest number of matrix
        high = matrix[n-1][n-1] #largest number of matrix
        res = -1

        while low <= high:
            mid = low + (high - low) // 2

            count = check(mid)

            if count < k:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        
        return res



        