class Solution:
    def fib(self, n: int) -> int: #prev two sum
        if n <= 1: #base case
            return n
        
        return self.fib(n-1) + self.fib(n-2) #recursive case

        