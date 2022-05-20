class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 -1
        
        minus = False
        
        if x < 0:
            x = x * -1
            minus = True
        
        reversed = 0
        
        while x != 0:
            m = x % 10    
            x = x // 10
            
            reversed = reversed * 10 + m
        
        
        if minus:
            reversed *= -1
        
        if reversed > MIN and reversed < MAX:
            return reversed
        
        return 0