class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False

        for i in range(len(intervals)):
            start1 = intervals[i][0]
            start2 = newInterval[0]
            if inserted == False and start1 >= start2:
                res.append(newInterval)
                inserted = True
            res.append(intervals[i]) #new one with one extra pair 

        if inserted == False:
            res.append(newInterval) #agr koi positn mle hi na insert ke lye toh last m insert

        ans = [] #for store new inserted and merged array
        res.sort(key = lambda x:x[0])
        start1 = res[0][0]
        end1 = res[0][1]

        for i in range(1,len(res)):
            start2 = res[i][0]
            end2 = res[i][1]
            if end1 >= start2:
                end1 = max(end1,end2)   
            else:
                ans.append([start1, end1])
                start1 = start2
                end1 = end2

        ans.append([start1, end1])
        return ans

        


        