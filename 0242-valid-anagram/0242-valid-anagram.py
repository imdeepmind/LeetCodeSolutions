from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)

        if n1 != n2:
            return False
        
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1
        
        for c in t:
            freq[c] -= 1
        
        for key, value in freq.items():
            if value != 0:
                return False
        
        return True