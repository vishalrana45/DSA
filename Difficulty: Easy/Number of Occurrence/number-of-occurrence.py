class Solution:
    def countFreq(self, arr, target):
        #position of first occurrence
        n = len(arr)
        low = 0
        high = n - 1
        first = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                first = mid
                high = mid - 1
                
        #position of last occurrence
        low = 0
        high = n - 1
        last = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                last = mid
                low = mid + 1  
        
        #target not found then we need to return 0
        if first == -1: #-1 because there is no value found that replace -1 which we take in starting
            return 0
            
        occurrence = last - first + 1 #formula to found index from first to last occurrence
        return occurrence 