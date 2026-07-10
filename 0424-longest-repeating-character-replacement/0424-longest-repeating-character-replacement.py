from typing import List
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        res = 0
        fre = {}
        for high in range(len(s)):
            fre[s[high]] = fre.get(s[high],0)+1
            length =  high-low+1
            maxfre = max(fre.values())
            diff = length - maxfre

            if diff > k:
                fre[s[low]]-=1
                low+=1

            else:
                res = max(res,length)

        return res
        