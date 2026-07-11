class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        if total - nums[0] == 0: #check index 0 separately
            return 0
        for i  in range(1,len(nums)):
            left += nums[i-1]
            right = total - nums[i] - left
            if left == right:
                return i
        return -1
        