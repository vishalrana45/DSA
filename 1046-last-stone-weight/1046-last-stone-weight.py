import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first == second:
                continue
            else:
                heapq.heappush(heap, -(first - second))
                
        return -heap[0] if heap else 0
        