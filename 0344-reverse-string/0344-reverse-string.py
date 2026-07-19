class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
        
        i = 0
        while len(stack) > 0:
            s[i] = stack.pop()
            i += 1
        
        return s

        