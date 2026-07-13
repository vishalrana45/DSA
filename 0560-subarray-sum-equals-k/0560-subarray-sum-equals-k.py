class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        prefix = 0 
        count = 0
        for num in nums:
            prefix += num
            if prefix - k in prefix_sum:
                count += prefix_sum[prefix - k]
            if prefix in prefix_sum:
                prefix_sum[prefix] += 1
            else:
                prefix_sum[prefix] = 1
        return count
