from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if s1 == s2: return True

        n1 = len(s1)
        n2 = len(s2)

        s1Freq = Counter(s1)

        for i in range(n2-n1+1):
            if Counter(s2[i:i+n1]) == s1Freq:
                return True
        
        return False
