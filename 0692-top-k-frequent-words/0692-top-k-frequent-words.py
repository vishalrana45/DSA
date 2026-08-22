import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        freq = {}

        for i in range(len(words)):
            freq[words[i]] = freq.get(words[i], 0) + 1
        
        for word, f in freq.items():
            heapq.heappush(heap, (-f, word)) #agr heap ke andr freq same ho jata h to samller wle ko remove kr deta hh toh neg. liya hh

        ans = []

        for i in range(k):
            f, word = heapq.heappop(heap)
            ans.append(word)

        return ans

        