class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #here it is not necessary a mountain
        n = len(nums)
        low = 0
        high = n - 1
        res = -1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid+1]: #here last and first element can be peak
                high = mid
            else:
                low = mid + 1
        
        return low #high can also return because at the end both are equal