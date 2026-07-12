class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0:-1} #hashmap
        zero = 0
        one = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            diff = zero - one
            
            if diff in map:
                res = max(res,i-map[diff])
            else:
                map[diff] = i
        return res
            


        