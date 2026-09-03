class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def fun(choice, index, n):
            if index == n:
                res.append(choice.copy())
                return 
            
            #Look at all possible substrings starting from index
            for next_idx in range(index + 1, n + 1):
                sub = s[index:next_idx]

                #Check if the substring is a palindrome
                if sub == sub[::-1]:
                    choice.append(sub)
                    fun(choice, next_idx, n)
                    choice.pop()

        fun([], 0, len(s))
        return res
        