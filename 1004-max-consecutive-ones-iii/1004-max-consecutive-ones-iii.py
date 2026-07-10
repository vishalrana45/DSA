class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = 0
        res = 0
        fre = {}
        for high in range(len(nums)):
            fre[nums[high]] = fre.get(nums[high],0)+1

            while fre.get(0,0)>k:
                fre[nums[low]]-=1
                low+=1
             
            res = max(res,high-low+1)

        return res

