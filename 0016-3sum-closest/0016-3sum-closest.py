from typing import List
import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0 #Store sum not list
        n = len(nums)
        max_diff = float('inf')

        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < max_diff:
                    max_diff = diff
                    result = sum

                if sum == target:
                    return sum
                    
                elif sum < target:
                    left+=1
                    
                else:
                    right-=1
                    
        return result
                

        