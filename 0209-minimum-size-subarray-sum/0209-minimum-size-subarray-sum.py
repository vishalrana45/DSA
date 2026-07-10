class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        min_len = float('inf')

        for i in range(len(nums)):
            sum = sum + nums[i]  #Hiring
            while sum >= target:
                min_len = min(min_len,i-left+1)
                sum -= nums[left] #Firing
                left+=1
        if min_len == float('inf'):
            return 0

        return min_len


        