class Solution:
    def sumOfDigits(self, n): #by recursion
        if n == 0:
            return 0
            
        d = n % 10
        n = n // 10
        ans = self.sumOfDigits(n)
        
        return ans + d
        
        
        