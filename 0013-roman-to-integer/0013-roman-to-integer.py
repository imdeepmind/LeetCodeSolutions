class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        l = 0

        while len(s) > l:
            c = s[l]

            if len(s) > l+1:
                nxt = s[l+1]
                if c == "I":
                    if nxt == "V":
                        res += 4
                        l += 2
                        continue
                    elif nxt == "X":
                        res += 9
                        l += 2
                        continue
                elif c == "X":
                    if nxt == "L":
                        res += 40
                        l += 2
                        continue
                    elif nxt == "C":
                        res += 90
                        l += 2
                        continue
                elif c == "C":
                    if nxt == "D":
                        res += 400
                        l += 2
                        continue
                    elif nxt == "M":
                        res += 900
                        l += 2
                        continue
                
            res += mapper[c]
            l += 1

        return res