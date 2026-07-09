class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count =  {0:1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num
            
            if (prefix - k) in prefix_count:
                count += prefix_count[prefix - k]
            
            if prefix in prefix_count:
                prefix_count[prefix] += 1
            else:
                prefix_count[prefix] = 1   

        return count