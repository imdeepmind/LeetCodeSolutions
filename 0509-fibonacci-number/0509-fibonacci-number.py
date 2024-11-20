class Solution:
    def fib(self, n: int) -> int:
        def find_fib(n, a=0, b=1):
            if n==0: return 0
            if n==1: return b
           
            a += b
            return find_fib(n-1, b, a)
       
        return find_fib(n)
