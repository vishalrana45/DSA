import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for f, num in heap]

        
        