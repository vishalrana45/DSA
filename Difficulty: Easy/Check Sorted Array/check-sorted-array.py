class Solution:
    def isSorted(self, arr):
        def check(i):
            
            if i >= len(arr)-1:
                return True
            
            if arr[i] > arr[i+1]:
                return False
            
            return check(i+1)
        
        return check(0)