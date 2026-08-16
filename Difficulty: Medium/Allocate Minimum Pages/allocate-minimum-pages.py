class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        
        if n < k: #agr books kaam hh students se to distribution possible nhi hh
            return -1
        
        def bookdis(mid):
            student = 1
            page = 0
            
            for i in range(len(arr)):
                if page + arr[i] <= mid:
                    page = page + arr[i]
                else:
                    student += 1
                    page = arr[i]
                    
                    if student > k:
                        return False
                    
            return True
        
        low = max(arr)
        high = sum(arr)
        res = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if bookdis(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return res 
        
