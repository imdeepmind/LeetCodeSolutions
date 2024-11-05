import re

class Solution:
    def actual_conversion(self, number: str, is_negative: bool):
        result = 0

        for index, c in enumerate(number):
            alpha = 10**(len(number) - (index+1))
            result += int(c) * alpha
        
        if is_negative:
            result *= -1
        
        return result
    
    def bullshit_check(self, s: str):
        can_accept_flag = True
        is_negative = False

        s = s.strip()

        if not s:
            return "0", is_negative
        
        if s[0] == "+":
            s = s[1:]
            can_accept_flag = False
        
        if not s:
            return "0", is_negative

        if not can_accept_flag and s[0] == "-":
            return "0", is_negative
        
        if not s:
            return "0", is_negative
            

        if s[0] == "-":
            is_negative = True
            s = s[1:]
        
        if not s:
            return "0", is_negative
            

        for index, c in enumerate(s):
            if not re.search('[0-9]', c):
                s = s[0:index]
        
        if not s:
            return "0", is_negative
            
        return s, is_negative

    def bullshit_range_check(self, result):
        if result <=-2147483648:
            return -2147483648

        if result >= 2147483648:
            return 2147483647
        
        return result

    def myAtoi(self, s: str) -> int:
        s, is_negative = self.bullshit_check(s)
        result = self.actual_conversion(s, is_negative)
        return self.bullshit_range_check(result)