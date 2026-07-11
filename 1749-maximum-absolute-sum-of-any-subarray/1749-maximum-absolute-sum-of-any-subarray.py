class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        curr_max_sum = nums[0]
        curr_min_sum = nums[0]

        for i in range(1,len(nums)):
            curr_max_sum = max(nums[i], nums[i] + curr_max_sum)
            max_sum = max(max_sum, curr_max_sum)

            curr_min_sum = min(nums[i], nums[i] + curr_min_sum)
            min_sum = min(min_sum, curr_min_sum)

        return max(max_sum, abs(min_sum))


       