class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        neg = []
        pos = []

        #Sep. two array
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        #If commplete array is negative
        if len(pos) == 0: #No positive elements
             res = [x * x for x in neg]
             res.reverse()
             return res
        
        #if complete array is positive
        if len(neg) == 0: #No neg. element
            res = [x * x for x in pos]
            return res
        
        #If both neg. and pos. exists
        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]
        n = len(neg)
        m = len(pos)
        i = 0
        j = 0
        res = []
        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        
        #If neg have 2 elements and pos have five then neg compl. soon but elemts left in pos so.. and vice verse..
        while i < n:
            res.append(neg[i])
            i+=1
        while j < m:
            res.append(pos[j])
            j+=1
        return res


            


        