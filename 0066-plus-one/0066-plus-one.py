class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        res = []

        for i in range(len(digits)-1, -1, -1):
            alpha = carry + digits[i]
            carry = 0

            if alpha > 9:
                alpha %= 10
                carry = 1
            
            res.append(alpha)
        
        if carry:
            res.append(carry)

        return res[::-1]


            