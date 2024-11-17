class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = False

        for i in range(len(digits) - 1, -1, -1):
            if carry:
                digits[i] += 1
                carry = False
                
            if digits[i] >= 10:
                carry = True
                digits[i] = digits[i] - 10
        
        if carry:
            return [1] + digits

        return digits