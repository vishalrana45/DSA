class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[n-1]:
                low = mid + 1
            else:
                high = mid - 1
            
        return nums[low]
        
        