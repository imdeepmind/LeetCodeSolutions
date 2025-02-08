class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        res = []
        n = len(digits)
        carry = 0

        for i in range(n-1, -1, -1):
            alpha = digits[i] + carry
            carry = 0

            if alpha >= 10:
                alpha %= 10
                carry = 1
            
            res.append(alpha)
        
        if carry:
            res.append(1)
        
        return res[::-1]