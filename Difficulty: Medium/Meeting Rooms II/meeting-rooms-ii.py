class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        i = 0
        j = 0
        room = 0
        res = 0
        n = len(start)
        m = len(end)
        
        while i < n and j < m:
            if start[i] < end[j]:
                room += 1
                res = max(res,room)
                i += 1
                
            else:
                room -= 1
                j += 1
        
        return res
        
