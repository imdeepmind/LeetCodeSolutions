class Solution:
    def isValid(self, s: str) -> bool:
        opp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        left_stack = []
        right_stack = []

        for c in s:
            if c in ("(", "{", "["):
                left_stack.append(c)
            else:
                if left_stack and left_stack[-1] == opp[c]:
                    del left_stack[-1]
                else:
                    right_stack.append(c)
        
        return not (len(left_stack) > 0 or len(right_stack) > 0)
