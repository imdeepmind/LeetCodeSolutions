class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opp = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for c in s:
            if c in opp:
                stack.append(c)
            else:
                if stack and opp[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0