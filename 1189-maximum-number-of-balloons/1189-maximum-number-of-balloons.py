class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = {}
        have = {}

        for ch in text:
            have[ch] = have.get(ch,0) + 1
        
        for ch in "balloon":
            need[ch] = need.get(ch,0) + 1
        
        ans = float("inf")
        for ch in need:
            ans = min(ans,have.get(ch,0) // need[ch])

        return ans
            

        