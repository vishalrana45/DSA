class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        fre = {}
        n = len(s)
        res = 0

        for right in range(n):
            fre[s[right]] = fre.get(s[right],0)+1
            while fre[s[right]]>1:
                fre[s[left]]-=1
                if fre[s[left]]==0:
                    del fre[s[left]]
                left+=1

            res = max(res,right-left+1)
        
        return res
