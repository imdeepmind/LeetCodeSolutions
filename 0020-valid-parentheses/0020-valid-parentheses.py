class Solution:
    def isValid(self, s: str) -> bool:
        left_ps = []
        right_ps = []

        opp = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }

        for c in s:
            if c in ('(', '{', '['):
                left_ps.append(c)
            else:
                if left_ps and left_ps[-1] == opp[c]:
                    del left_ps[-1]
                else:
                    right_ps.append(c)
        
        return len(left_ps) == 0 and len(right_ps) == 0

