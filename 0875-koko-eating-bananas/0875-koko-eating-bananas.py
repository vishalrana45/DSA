class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            hours = 0
            for pile in piles:
                hours += pile // mid
                if pile % mid != 0:
                    hours += 1

            if hours > h:
                low =  mid + 1
            else:
                high = mid - 1
        
        return low
                
        