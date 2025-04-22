class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            last = (n >> i) & 1
            res += last << (31 - i)
        
        return res
