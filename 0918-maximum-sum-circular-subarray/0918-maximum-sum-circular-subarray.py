class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        minsum = nums[0]
        currmaxsum = nums[0]
        currminsum = nums[0]
        totalsum = nums[0]

        for i in range(1,len(nums)):
            currmaxsum = max(nums[i],currmaxsum + nums[i])
            maxsum = max(currmaxsum,maxsum)

            currminsum = min(nums[i],currminsum + nums[i])
            minsum = min(currminsum,minsum)

            totalsum += nums[i]

        circularsum = totalsum - minsum

        if circularsum == 0:
            return maxsum
            
        return max(maxsum,circularsum)




        
        