class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        sum =  0
        count = 0
        for num in nums:
            sum += num
            rem = sum % k
            if rem < 0:
                rem = rem + k #To handle the neg. elements
            
            if rem in prefix_sum:
                count += prefix_sum[rem]
                prefix_sum[rem] += 1
            else:
                prefix_sum[rem] = 1
        return count
        