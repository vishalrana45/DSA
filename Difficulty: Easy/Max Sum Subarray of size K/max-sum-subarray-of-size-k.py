class Solution:
    def maxSubarraySum(self, arr, k):
        low = 0
        high = k-1
        n = len(arr)
        sum = 0
        
        for i in range(k):
            sum = sum + arr[i]
            
        res = sum
        
        while high < n-1:
            low+=1
            high+=1
            sum = sum - arr[low-1] + arr[high]
            res = max(res,sum)
            
        return res
            