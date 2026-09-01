class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def fun(choice, index, n):
            if index == n:
                res.append(choice.copy())
                return 
        
            for num in nums:
                if num not in choice:
                    choice.append(num)
                    fun(choice, index + 1,n)
                    choice.pop()
            
        fun([], 0, len(nums))
        return res
        