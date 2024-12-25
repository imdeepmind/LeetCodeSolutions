class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        
        if num2 == "0":
            return num1
        
        i, j = len(num1) - 1, len(num2) - 1

        res = ""
        carry = 0

        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0

            alpha = x + y + carry
            carry = 0

            if alpha > 9:
                carry = 1
                alpha = alpha % 10
            
            res += str(alpha)

            i -= 1
            j -= 1

        if carry == 1:
            res += "1"

        return res[::-1]
