class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                
            else:
                if stack[-1] == s[i]: #-1 is the last stored elem. in the stack
                    stack.pop()
                else:
                    stack.append(s[i])
        
        return "".join(stack) #stack contain list of ch ['c','a'] but join retn string "ca"

        
        

        