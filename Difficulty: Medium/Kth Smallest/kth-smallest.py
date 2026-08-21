
import heapq #for max heap as in py their is not max heap and store neg value in it

class Solution:
    def kthSmallest(self, arr, k):
        heap = []
        
        for i in range(k): #starting ke k elemnts ko push krna hh
            heapq.heappush(heap, -arr[i]) #neg to store max. value
        
        for i in range(k,len(arr)): #jo left elements hh ab unhe top wle se compare krna hh
            if arr[i] >= -heap[0]:
                continue
            #agr top wle se chota hh to heap ke andr push krna hoga aur top wle ko pop
            heapq.heappop(heap)
            heapq.heappush(heap, -arr[i])
            
        return -heap[0]
        
