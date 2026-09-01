class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = [] #temporary
        
        def backtrack(open, close):
            if open == n and close == n:
                res.append("".join(path))
                return 
            
            if open < n:
                path.append("(")
                backtrack(open + 1, close)
                path.pop()  #decision reverse
            
            if close < open:
                path.append(")")
                backtrack(open, close + 1)
                path.pop()  #decision reverse
            
        backtrack(0, 0) #initial condition when open and close still zero
        return res


        

        