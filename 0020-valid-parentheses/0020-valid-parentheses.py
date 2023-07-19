class Solution:
    def isValid(self, s: str) -> bool:
        start_bracket = []
        end_bracket = []
        
        start_bracket_sign = "({["
        opp_brackets = {
            '(': ')',
            ')': '(',
            '{': '}',
            '}': '{',
            '[': ']',
            ']': '['
        }
        
        for c in s:
            if c in start_bracket_sign:
                start_bracket.append(c)
            else:
                if len(start_bracket) > 0 and start_bracket[-1] == opp_brackets[c]:
                    del start_bracket[-1]
                else:
                    end_bracket.append(c)
            
        return len(start_bracket) == 0 and len(end_bracket) == 0
    