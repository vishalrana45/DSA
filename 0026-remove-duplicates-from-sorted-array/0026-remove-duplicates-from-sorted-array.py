class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        unique = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j+=1
                continue
            else:
                i+=1
                nums[i]=nums[j]
                unique+=1
                j+=1
        return unique
        