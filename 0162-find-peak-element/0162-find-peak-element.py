class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        res = -1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        
        return low