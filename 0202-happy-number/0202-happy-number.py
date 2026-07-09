class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(n):
            sum = 0
            while n > 0:
                d = n % 10
                n = n // 10
                sum = sum + d * d
            return sum
        
        slow = n
        fast = n
        while True:
            slow = fun(slow)
            fast = fun(fast)
            fast = fun(fast)
            if slow == fast: #Cycle detect not a happy number
                break
        return slow == 1


        