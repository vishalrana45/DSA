class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        left = 0
        fre = {}
        res = -1
        
        for high in range(n):
            fre[s[high]] = fre.get(s[high],0)+1
            
            while len(fre) > k:
                fre[s[left]]-=1
                if fre[s[left]]==0:
                    del fre[s[left]]
                left+=1
            
            if len(fre)==k:
                res = max(res,high-left+1)
        
        return res