from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = defaultdict(int)

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in t:
            freq[c] -= 1
        
        for key, value in freq.items():
            if value != 0:
                return False
        
        return True
        
