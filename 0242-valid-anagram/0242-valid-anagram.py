from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)

        if n1 != n2:
            return False
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for i in range(n1):
            s_freq[s[i]] += 1
            t_freq[t[i]] += 1
        
        for key, value in s_freq.items():
            if t_freq[key] != value:
                return False
        
        return True
