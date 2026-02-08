from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}

        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        for c in t:
            freq[c] = freq.get(c, 0) - 1
        
        for key, value in freq.items():
            if value != 0:
                return False
        
        return True