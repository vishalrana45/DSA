import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freq = {}
        free = {}
        res = []

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
            free[task] = 1

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))
        
        seat = 1
        wait = [] #agr koi kisi seat pr nhi baith skte due to free so kuch time ke liye yha store kr denge again push kr denge heap mm

        while heap or wait:
            while wait and wait[0][0] <= seat: # put free tasks back into heap
                free_time, count, ch = heapq.heappop(wait)
                heapq.heappush(heap, (count, ch))

            if not heap: #age sb wait mm chla gya to uss seat pr koi nhi aa skta
                seat += 1
                continue

            count, ch = heapq.heappop(heap)

            if free[ch] > seat:
                heapq.heappush(wait, (free[ch], count, ch))
                continue

            res.append(ch)
            count += 1 #+ because of max heap, freq of that ch

            if count != 0: #if ch still have freq
                free[ch] = seat + n + 1
                heapq.heappush(heap, (count, ch))
            
            seat += 1
        
        return seat - 1 #1 seat extra ho jayegi toh









             
        