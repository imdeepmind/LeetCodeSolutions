class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}

        def count(n):
            if n == 0: return 1
            if n == 1: return 1

            if n in ways: return ways[n]
            
            res = count(n-1) + count(n-2)
            ways[n] = res
            
            return res
        
        return count(n)