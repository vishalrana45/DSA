class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(mid):
            rows = m
            cols = n

            row = rows - 1 #start from any corner
            col = 0
            count = 0 #to check how many element before guess is it k or not

            while row >= 0 and col < cols:
                if (row + 1) * (col + 1) <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            
            return count
        
        low = 1 #smallest number of matrix
        high = m * n #largest number of matrix
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



        
        