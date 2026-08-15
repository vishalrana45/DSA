class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()
        
        def canPlace(mid):
            cows = 1 #1 cow is already placed
            prevpos = arr[0] #at first pos cow 1 is placed
        
            for i in range(1,len(arr)):
                dist = arr[i] - prevpos
                
                if dist >= mid:
                    cows += 1
                    prevpos = arr[i]
                
                if cows >= k:
                    return True
                    
            return False
        
        n = len(arr)   
        low = 0
        high = arr[-1] - arr[0] #max distance b/t two cows last and first
        res = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if canPlace(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
       
        