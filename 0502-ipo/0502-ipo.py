import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []

        for i in range(len(capital)):
            projects.append((capital[i], profits[i])) #creating pair

        projects.sort()

        heap = []
        index = 0

        for _ in range(k): #we can choose only k projects
            while index < len(projects):
                if projects[index][0] > w:
                    break
                else:
                    heapq.heappush(heap, -projects[index][1])
                    index += 1
                
            if not heap: #if heap is empty
                break

            profits = -heapq.heappop(heap) #max heap, give top
            w += profits #profit is added in reserve capital
            
        return w



        