class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        j = 0 
        k = n-1
        while j <= k:
            if nums[j] == 1:
                j+=1
            
            elif nums[j] == 2:
                nums[j],nums[k] = nums[k],nums[j]
                k-=1
            
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1


       
        