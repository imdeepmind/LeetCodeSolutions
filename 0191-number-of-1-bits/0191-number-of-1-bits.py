class Solution:
    def hammingWeight(self, n: int) -> int:
        no_bits = 0

        while n:
            if n & 1:
                no_bits += 1
            n = n >> 1
        
        return no_bits