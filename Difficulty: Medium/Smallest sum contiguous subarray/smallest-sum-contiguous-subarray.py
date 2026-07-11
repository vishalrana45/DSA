class Solution:
    def smallestSumSubarray(self, A, N):
        i = 0
        best = A[0]
        ans = A[0]
        for i in range(1,N):
            v1 = best + A[i]
            v2 = A[i]
            best = min(v1,v2)
            ans = min(ans,best)
        return ans
        