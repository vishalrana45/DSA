class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        i = 0
        n = len(arr)
        
        count = 0
        
        for i in range(n-2):
            left = i+1
            right = n-1
            
            while left < right:
                add = arr[i]+arr[left]+arr[right]
                if add < sum:
                    count+=(right - left)
                    left+=1
                
                else:
                    right-=1
                    
        return count
                    