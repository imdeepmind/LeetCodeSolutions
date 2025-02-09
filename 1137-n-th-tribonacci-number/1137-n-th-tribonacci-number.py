class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]

        if n < 3:
            return res[n]

        for i in range(3, n+1):
            res = [res[1], res[2], sum(res)]

        return res[-1]