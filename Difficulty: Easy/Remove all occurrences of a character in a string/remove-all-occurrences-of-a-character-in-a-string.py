class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        ans = []
        
        def solve(i):
            if i == len(s):
                return
            
            if s[i] != c:
                ans.append(s[i])
                
            solve(i+1)
        
        solve(0)
        
        return ''.join(ans)
                
        
        
        
        