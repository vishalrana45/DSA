class Solution:
    def longestPalindrome(self, s: str) -> int:
        fre = {}
        res = 0
        has_odd = False

        for ch in s:
            fre[ch] = fre.get(ch,0) + 1

        for ch in fre:
            if fre[ch] % 2 == 0:
                res += fre[ch]
            else:
                res += fre[ch] - 1
                has_odd = True
        
        if has_odd:
            res += 1
        
        return res

        