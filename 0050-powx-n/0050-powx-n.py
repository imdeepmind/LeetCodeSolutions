class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = calc(x*x, n//2)

            return res * x if n % 2 else res

        res = calc(x, abs(n))

        return res if n >= 0 else 1 / res 