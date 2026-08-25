import heapq

class Solution:
    def mergeArrays(self, mat):
        heap = []
        n =  len(mat)
        m = len(mat[0])
        res = []
        
        for i in range(n): #push first element of each array
            heapq.heappush(heap, (mat[i][0], i, 0))
            
        while heap: #jb tk heap empty na ho jaye
            value, row, col = heapq.heappop(heap)
            res.append(value)
            
            if col+1 < m:
                heapq.heappush(heap, (mat[row][col+1], row, col+1))
    
        return res
        