class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        for n in range(min(l1, l2), 0, -1):
            if l1 % n == 0 and l2 % n == 0:
                f1, f2 = l1 // n, l2 // n

                if str1 == f1 * str1[:n] and str2 == f2 * str1[:n]:
                    return str1[:n]
        
        return ""