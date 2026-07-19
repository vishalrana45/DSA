class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        res = []

        for i in range(len(s)):
            stack.append(s[i])
        
        while len(stack) > 0:
            res.append(stack.pop())

        for i in range(len(s)):
            s[i] = res[i]
        
        return s


        