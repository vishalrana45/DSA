class Solution:
    def findCeil(self, arr, x):
        n = len(arr)
        low = 0
        high = n - 1
        res = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] < x:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
            
        return res
        
        