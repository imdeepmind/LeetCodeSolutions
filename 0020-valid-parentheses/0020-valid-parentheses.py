class Solution:
    def isValid(self, s: str) -> bool:
        start_bracket = []
        end_bracket = []

        opp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in ('(', '[', '{'):
                start_bracket.append(c)
            else:
                if start_bracket and start_bracket[-1] == opp[c]:
                    start_bracket.pop()
                else:
                    end_bracket.append(c)

        return not (len(start_bracket) > 0 or len(end_bracket) > 0)
