class Solution:
    def romanToInt(self, s: str) -> int:
        obj = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        jump = False
        
        for index, n in enumerate(s):
            if jump:
                jump = False
                continue
                
            if len(s) > index+1:
                next_c = s[index+1]
                
                if n == 'I' and next_c in ('X', 'V'):
                    num += 4 if next_c == 'V' else 9
                    jump = True
                    continue
                elif n == 'X' and next_c in ('L', 'C'):
                    num += 40 if next_c == 'L' else 90
                    jump = True
                    continue
                elif n == 'C' and next_c in ('D', 'M'):
                    num += 400 if next_c == 'D' else 900
                    jump = True
                    continue

            num += obj[n]
        
        return num