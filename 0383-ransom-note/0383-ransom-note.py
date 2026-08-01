class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = {}
        need = {}

        for num in ransomNote:
            need[num] = need.get(num,0) + 1
        for num in magazine:
            have[num] = have.get(num,0) + 1
        
        for ch in need:
            if have.get(ch,0) < need[ch]:
                return False
            
        return True
                
            
    
        