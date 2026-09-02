class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def fun(choice, index, n, sum):
            if index == n:
                if sum == target:
                    res.append(choice.copy())
                return 
                
            fun(choice, index + 1, n, sum) #agr koi element nhi lena hh

            if candidates[index] + sum <= target: #then again usse no. se targte mil bhi skta hh
                choice.append(candidates[index])
                sum = sum + candidates[index]
                fun(choice, index, n, sum)
                choice.pop()

                sum = sum - candidates[index] #use to undo the choice

        fun([], 0, len(candidates), 0) 
        return res

            

            
        