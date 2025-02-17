from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        if n1 != n2:
            return False
        
        for i in range(n1):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1
        
        for key, value in freq_s.items():
            if value != freq_t[key]:
                return False
        
        return True