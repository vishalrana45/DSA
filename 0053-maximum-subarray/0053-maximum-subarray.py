class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        best_end = 0
        ans = nums[0]
        for i in range(len(nums)):
            v1 = best_end + nums[i]
            v2 = nums[i]
            best_end = max(v1,v2)
            ans = max(ans,best_end)
        return ans

        