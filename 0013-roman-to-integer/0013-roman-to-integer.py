class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            'I': 1,
            'V': 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        val = 0
        i = 0

        while len(s) > i:
            c = s[i]
            nxt_c = s[i+1] if len(s)-1 > i else 'NA'

            if c == 'I':
                if nxt_c == 'V':
                    val += 4
                    i += 2
                    continue
                elif nxt_c == "X":
                    val += 9
                    i += 2
                    continue
            elif c == "X":
                if nxt_c == "L":
                    val += 40
                    i += 2
                    continue
                elif nxt_c == "C":
                    val += 90
                    i += 2
                    continue
            elif c == "C":
                if nxt_c == "D":
                    val += 400
                    i += 2
                    continue
                elif nxt_c == "M": 
                    val += 900
                    i += 2
                    continue
            
            val += mapper[c]
            i += 1

        return val