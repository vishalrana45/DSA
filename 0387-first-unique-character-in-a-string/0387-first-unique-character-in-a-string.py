class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_list = {}

        for num in s:
            my_list[num] = my_list.get(num, 0) + 1

        i = 0
        for ch in s:
            if my_list[ch] == 1:
                return i
            i += 1
            
        return -1
        