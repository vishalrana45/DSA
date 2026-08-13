class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > nums[n-1]: #part2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    if nums[0] > target:
                        low = mid + 1
                    else:
                        high = mid - 1
            
            else: #part1
                if nums[mid] > target:
                    high = mid - 1
                else:
                    if nums[n-1] < target:
                        high = mid - 1
                    else:
                        low = mid + 1
        
        return -1
        