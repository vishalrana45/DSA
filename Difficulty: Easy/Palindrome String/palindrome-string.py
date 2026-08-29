class Solution:
    def isPalindrome(self, s):
        def check(left, right): #left = 0 and right = len(s) - 1
            
            if left >= right: #base case
                return True
                
            if s[left] != s[right]:
                return False
            
            return check(left+1, right-1)
        
        return check(0, len(s)-1)
