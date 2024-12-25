class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        
        if num2 == "0":
            return num1
        
        n1 = len(num1)
        n2 = len(num2)

        # Find the big number in length
        big = ""
        small = ""
        if n1 > n2:
            big = num1
            small = num2
        else:
            big = num2
            small = num1
        
        # Iterate through the big
        big = big[::-1]
        small = small[::-1]

        res = ""
        carry = 0

        for index, b_num in enumerate(big):
            s_num = "0"
            if len(small) > index:
                s_num = small[index]
            
            alpha = int(s_num) + int(b_num) + carry
            carry = 0

            if alpha > 9:
                carry = 1
                alpha = alpha % 10
            
            res += str(alpha)

        if carry == 1:
            res += "1"
            
        return res[::-1]
