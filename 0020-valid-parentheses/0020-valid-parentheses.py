class Solution:
    def isValid(self, s: str) -> bool:
        start_params = []
        end_params = []

        opp = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }

        for c in s:
            if c in ['(', '{', '[']:
                start_params.append(c)
            else:
                if start_params and start_params[-1] == opp[c]:
                    del start_params[-1]
                else:
                    end_params.append(c)

        return len(start_params) == 0 and len(end_params) == 0
