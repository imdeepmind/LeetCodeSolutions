class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def divide_numbers(n):
            divided_numbers = []
            
            while n > 26:
                n -= 1
                divided_numbers.append(n%26+65)
                n //= 26
                
            divided_numbers.append(n+64)
        
            return divided_numbers[::-1]
        
        divided_numbers = divide_numbers(columnNumber)
        res = ""

        for num in divided_numbers:
            res += chr(num)
        
        return res