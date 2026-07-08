class Solution:
    from typing import List
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n-2):
            #Skip duplication which is fixed
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    #Skip duplicate second elements
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
                    
                elif sum < 0:
                    left+=1
                
                else:
                    right-=1
                
        return res
        