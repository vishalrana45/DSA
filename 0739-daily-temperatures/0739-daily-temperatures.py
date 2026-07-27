class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n-1,-1,-1):

            while stack and temperatures[stack[-1]] <= temperatures[i]: #stack[-1] - top of stack and temperatures[stack[-1]] - temperature at that top
                stack.pop()

            if stack:
                res[i] = stack[-1] - i #top se kitne durr index pr value aaye so sub.

            stack.append(i) #we need to append index so use only [i] not temp[i]
            
        return res 

        