class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #for first occurrence
        n = len(nums)
        low = 0
        high = n - 1
        first = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else: #equal condn
                first = mid 
                high = mid - 1 #for first occurrence

        #for second occurrence         
        n = len(nums)
        low = 0
        high = n - 1
        last = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else: #equal condn
                last = mid 
                low = mid + 1 #for second occurrence
                
        return [first,last] 

        