class Solution:
    def letterCombinations(self, digits: str) -> List[str]: #here given no. are string type
        f = {}  #as dictionary
        f['2'] = 'abc'
        f['3'] = 'def'
        f['4'] = 'ghi'
        f['5'] = 'jkl'
        f['6'] = 'mno'
        f['7'] = 'pqrs'
        f['8'] = 'tuv'
        f['9'] = 'wxyz'
        res = []

        if not digits: #to handle the empty string
            return []

        def fun(choice, index, n):
            if index == n:
                res.append(choice)
                return
                
            for ch in f[digits[index]]:
                fun(choice + ch, index + 1, n)

        fun("", 0, len(digits)) #initial call to your recursive functio  
        return res
