from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if s1 == s2: return True

        n1 = len(s1)
        n2 = len(s2)

        s1Freq = Counter(s1)
        windowFreq = Counter(s2[:n1])

        for i in range(1, n2-n1+1):
            if s1Freq == windowFreq: return True

            windowFreq[s2[i-1]] -= 1
            windowFreq[s2[i+n1-1]] += 1
            
        return  s1Freq == windowFreq
