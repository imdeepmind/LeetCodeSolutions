class Solution:
    def isValid(self, s: str) -> bool:
        start_stack = []
        end_stack = []
        opp = {
            '(': ')',
            ')': '(',
            '{': '}',
            '}': '{',
            '[': ']',
            ']': '['
        }
        
        
        for p in s:
            if p in ('(', '{', '['):
                start_stack.append(p)
            else:
                if len(start_stack) > 0 and start_stack[-1] == opp[p]:
                    del start_stack[-1]
                else:
                    end_stack.append(p)
        
        return True if len(start_stack) == 0 and len(end_stack) == 0 else False
