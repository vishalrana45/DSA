class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]
        one_del = float('-inf')
        res = arr[0]
        for i in range(1,len(arr)):
           prev_no_del = no_del
           no_del = max(no_del + arr[i],arr[i])
           one_del = max(prev_no_del,one_del + arr[i])
           res = max(res,no_del,one_del)
        return res
        