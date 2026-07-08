class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        pair = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                if pair < 2:
                    i+=1
                    nums[i] = nums[j]
                    pair+=1
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
                pair=1
                j+=1
        return i+1
        