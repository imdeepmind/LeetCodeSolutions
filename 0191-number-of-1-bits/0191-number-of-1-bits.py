class Solution:
    def hammingWeight(self, n: int) -> int:
        noBits = 0
        while n:
            if n & 1:
                noBits += 1
            
            n >>= 1
        
        return noBits