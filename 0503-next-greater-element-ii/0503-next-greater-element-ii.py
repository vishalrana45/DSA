class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums   # make circular array normal
        stack = []
        res = [-1] * n

        for i in range(2*n-2,-1,-1):

            while stack and stack[-1] <= nums[i]: #stack -> not empty
                stack.pop()

            if i < n:
                if stack:
                    res[i] = stack[-1]
                    
            stack.append(nums[i])
        
        return res
        