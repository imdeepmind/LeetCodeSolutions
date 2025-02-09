class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1, n2 = len(a), len(b)
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = ""

        for i in range(max(n1, n2)):
            digitA = int(a[i]) if n1 > i else 0
            digitB = int(b[i]) if n2 > i else 0

            s = digitA + digitB + carry
            char = s % 2
            carry = s // 2

            res = str(char) + res
        
        if carry:
            res = "1" + res

        return res