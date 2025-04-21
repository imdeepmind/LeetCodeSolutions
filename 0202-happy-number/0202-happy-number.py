class Solution:
    def find_sum(self, n):
        res = []

        while n > 0:
            res.append((n % 10) ** 2)
            n //= 10
        
        return sum(res)

    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        
        n = self.find_sum(n)
        dp = set()

        while n != 1:
            n = self.find_sum(n)

            if n in dp:
                return False

            dp.add(n)
        
        return True
