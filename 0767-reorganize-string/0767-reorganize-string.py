import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = {}
        seat = 0 #let first seat for letter with higher freq
        res = []

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch)) #use max. heap


        while heap: #mtlb jb tk heap empty na ho jaye
            if seat == 0 or res[seat-1] != heap[0][1]: #check previous letter same or not if not same then append into next seat like abab
                freq, ch = heapq.heappop(heap) #pop the top lettter

                res.append(ch)
                seat += 1
                freq += 1 #pos.(+) beacuese freq is neg. in max. heap
                
                #ab freq i km ho gyi but if agr abhi bhi bchi hh to again push back kr do..
                if freq < 0: #still letter have freq but here we use samll as freq is neg.
                    heapq.heappush(heap, (freq,ch))
            
            else: #agr aabb hh first a second b ho gye to ab freq same ho jayegi toh decision bde ke acc. ho mtlb b aayega ab phir abb ho jayega glt
                first_freq, first_ch = heapq.heappop(heap)

                if not heap: #if now heap become empty
                    return ""
            
                freq, ch = heapq.heappop(heap) #pop the top lettter

                res.append(ch)
                seat += 1
                freq += 1  
                
                if freq < 0:
                    heapq.heappush(heap, (freq, ch))

                # Put first character back because we didn't use it
                heapq.heappush(heap, (first_freq, first_ch))

        return "".join(res)



                